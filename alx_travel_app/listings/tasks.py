from __future__ import absolute_import, unicode_literals
import logging
from datetime import datetime
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_booking_email_task(user_email, booking_id):
    try:
        send_mail(
            "Booking Confirmation",
            f"Your booking with ID {booking_id} has been successfully created!",
            "no-reply@alxtravelapp.com",
            [user_email],
        )
        logger.info(f"Email sent to {user_email} for booking {booking_id}")
        return f"Email sent to {user_email} for booking {booking_id}"
    except Exception as e:
        logger.error(f"Error sending email to {user_email}: {e}")
        raise
