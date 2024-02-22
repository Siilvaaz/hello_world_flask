# PubSub_Publisher.py

from google.cloud import pubsub_v1

def publish_message(project_id, topic_name, message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    future = publisher.publish(topic_path, data=message.encode('utf-8'))
    message_id = future.result()
    print(f"Published message to {topic_path}. Message ID: {message_id}")

if __name__ == '__main__':
    project_id = 'sandbox-anthos'
    topic_name = 'jenkins_poc'
    message = 'your_message_payload'
    publish_message(project_id, topic_name, message)
