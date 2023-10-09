from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post, Subscriber

from .send_email import send_email
from .tasks import send_email_task
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

# send_email_task.delay(text_html, to_email)
# Метод delay() используется в связке с Celery
# для асинхронного выполнения задач.

@receiver(post_save, sender=Post)
def create_post(sender, instance, created, **kwargs):
    if created:
        category_list = instance.postCategory.all()

        for category in category_list:
            subscriber_list = Subscriber.objects.filter(
                category=category
            )
            email_list = []
            for s in subscriber_list:
                to_email = s.user.email
                # send_email(text_html, to_email)
                email_list.append(to_email)
            text_base = '''
		    Вышел новый пост <br>
	        '''
            text_html = text_base.replace('{post_id}', str(instance.id))
            send_email_task.delay(text_html, email_list)


@receiver(post_save, sender=Post)
def save_post(sender, instance, **kwargs):
    category_list = instance.postCategory.all()

    for category in category_list:
        subscriber_list = Subscriber.objects.filter(
            category=category
        )
        email_list = []
        for s in subscriber_list:
            to_email = s.user.email
            # send_email(text_html, to_email)
            email_list.append(to_email)
        text_base = '''
        Вышел новый пост <br>
	'''
        text_html = text_base.replace('{post_id}', str(instance.id))
        send_email_task.delay(text_html, email_list)

        # удаление из кэша при изменении поста
        # cache key for {% cache 300 news post.id %}
        key = make_template_fragment_key('news', [instance.id])
        cache.delete(key)