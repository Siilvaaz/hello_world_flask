# PubSub_Publisher.py

import sys
from google.cloud import pubsub_v1

def publish_message(project_id, topic_name, input_payload):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    # Publishes a message
    future = publisher.publish(topic_path, data=input_payload.encode("utf-8"))
    message_id = future.result()

    # Write message ID to file
    with open('pubsub_ack.txt', 'w') as ack_file:
        ack_file.write(str(message_id))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} project_id topic_name input_payload")
        sys.exit(1)

    project_id = sys.argv[1]
    topic_name = sys.argv[2]
    input_payload = sys.argv[3]

    publish_message(project_id, topic_name, input_payload)
