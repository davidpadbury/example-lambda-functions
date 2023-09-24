from datetime import datetime
from typing import Optional
from dataclasses import dataclass
from htmlslacker import HTMLSlacker
from os import getenv
from time import sleep
import json
import feedparser
import boto3


@dataclass
class NewEntries:
    entries: list[dict]
    feed: dict


def fetch_new_entries(feed_source: str, since_published_date: Optional[datetime] = None) -> NewEntries:
    feed = feedparser.parse(feed_source)

    entries = sorted(feed.entries, key=lambda e: e.published_parsed)
    
    if since_published_date:
        entries = list(filter(lambda e: e.published_parsed > since_published_date, entries))

    return NewEntries(
        entries=entries,
        feed=feed['feed']
    )


def create_notification(entry: dict, feed: dict) -> dict:
    # custom notifications documentation: https://docs.aws.amazon.com/chatbot/latest/adminguide/custom-notifs.html
    return {
        'version': '1.0',
        'source': 'custom',
        'content': {
            'textType': 'client-markdown',
            'title': entry.title,
            'description': HTMLSlacker(entry.description).get_output().strip(),
            'nextSteps': [
                f'<{entry.link}|View Post>',
                f'<{feed["link"]}|View "{feed["title"]}" feed>'
            ]
        }
    }


def required_env(name: str) -> str:
    value = getenv(name)
    
    if not value:
        raise Exception(f'Missing environment variable [{name}]')

    return value


def publish_notifications(topic_arn: str, notifications: list[dict]):
    sns = boto3.client('sns')

    for notification in notifications:
        sns.publish(
            TopicArn=topic_arn,
            Message=json.dumps(notification)
        )
        # wait a tiny bit between each publish
        sleep(1)


def lambda_handler(event, context):
    feed = required_env('FEED_URL')
    topic_arn = required_env('SNS_TOPIC_ARN')

    new_entries = fetch_new_entries(feed)
    entries_to_publish = new_entries.entries[-3:]

    notifications = list(map(lambda e: create_notification(e, new_entries.feed), entries_to_publish))

    publish_notifications(topic_arn=topic_arn, notifications=notifications)

    return {
        'statusCode': 200,
        'body': f'Published {len(notifications)} notifications'
    }
