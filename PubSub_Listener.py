from google.cloud import pubsub_v1
import json
import sys
from datetime import datetime

def receive_messages(project_id, subscription_id, output_file):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    def callback(message):
        with open(output_file, 'w') as f:
            data = {
                "message_id": message.message_id,
                "data": message.data.decode('utf-8'),
                "attributes": dict(message.attributes),
                "publish_time": message.publish_time.isoformat(),  # Convert datetime to string
            }
            json.dump(data, f, indent=2)

        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...\nPress Ctrl+C to exit.")

    # Keep the main thread alive to continue listening for messages
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} project_id subscription_id output_file")
        sys.exit(1)

    project_id = sys.argv[1]
    subscription_id = sys.argv[2]
    output_file = sys.argv[3]

    receive_messages(project_id, subscription_id, output_file)
