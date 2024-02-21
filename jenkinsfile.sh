node{
    stage('Install dependencies'){
        sh """
        pwd
        pip3.10 install google-cloud-pubsub
        pip3.10 install google-cloud-storage
        pip3.10 install google-api-core
        pip3.10 install google-cloud-bigquery
        pip3.10 install pybase64
        """
    }
    stage('Git Clone'){
        sh """
        pwd
        rm -rf hello_world_flask
        git clone https://github.com/Siilvaaz/hello_world_flask -b main
        ls -lart
        """
    }
    stage('Get Input from GCS'){
        sh """
        pwd
        cd hello_world_flask
        python3.10 Get_Payload.py sandbox-anthos payload_repository gcs_folder input.json
        """
    }
    stage('Get Expected Output payload from GCS'){
        sh """
        pwd
        cd hello_world_flask
        python3.10 Get_Payload.py sandbox-anthos payload_repository gcs_folder expected_output.json
        """
    }
    stage('Publish to PubSub'){
        sh """
        pwd
        cd hello_world_flask
        python3.10 PubSub_Publisher.py sandbox-anthos input_pubsub_topic input.json
        ls -l
        echo "### pubsub message id ###"
        cat pubsub_ack.txt
        """
    }
    stage('Listen to PubSub'){
        sh """
        pwd
        cd GCP_Jenkins_Test_Utility
         python3.10 PubSub_Listener.py sandbox-anthos output_pubsub_topic-sub received_payload.json
         ls -l
         """
    }
    stage('Compare Payloads'){
        sh """
        pwd
        cd GCP_Jenkins_Test_Utility
        python3.10 Verify_Payload.py sandbox-anthos expected_output.json received_payload.json
    }
    
}