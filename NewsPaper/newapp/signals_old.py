from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post, Subscriber

from .send_email import send_email


@receiver(post_save, sender=Post)
def create_post(sender, instance, created, **kwargs):
    if created:
        category_list = instance.postCategory.all()

        for category in category_list:
            subscriber_list = Subscriber.objects.filter(
                category=category
            )

            for s in subscriber_list:
                text_base = '''
					Вышел новый пост <br>
					<a href="http://127.0.0.1:8000/news/{post_id}/">Читать пост</a>
				'''
                text_html = text_base.replace('{post_id}', str(instance.id))
                to_email = s.user.email
                send_email(text_html, to_email)


@receiver(post_save, sender=Post)
def save_post(sender, instance, **kwargs):
    category_list = instance.postCategory.all()

    for category in category_list:
        subscriber_list = Subscriber.objects.filter(
            category=category
        )

        for s in subscriber_list:
            text_base = '''
				Вышел новый пост <br>
				<a href="http://127.0.0.1:8000/news/{post_id}/">Читать пост</a>
			'''
            text_html = text_base.replace('{post_id}', str(instance.id))
            to_email = s.user.email
            send_email(text_html, to_email)