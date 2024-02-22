from google.cloud import pubsub_v1

def publish_message(project_id, topic_name, message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    # Convert message to bytes
    message_data = message.encode('utf-8')

    # Publish message
    future = publisher.publish(topic_path, data=message_data)
    message_id = future.result()

    print(f"Published message to {topic_path}. Message ID: {message_id}")

if __name__ == "__main__":
    # Your Google Cloud project ID
    project_id = "sandbox-anthos"

    # Name of the Pub/Sub topic
    topic_name = "jenkins_poc"

    # Path to the file containing the input payload
    file_path = "/var/lib/jenkins/workspace/test_utility_trigger/hello_world_flask/input.json"

    # Read input payload from the file
    with open(file_path, "r") as file:
        input_payload = file.read()

    # Publish the input payload to the Pub/Sub topic
    publish_message(project_id, topic_name, input_payload)
