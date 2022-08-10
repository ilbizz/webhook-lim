# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os
# Imports Python standard library logging
import logging
from flask import Flask, request
from google.cloud import pubsub_v1
from sys import getsizeof

app = Flask(__name__)


@app.route("/")
def hello_bizzabo():
    name = os.environ.get("NAME", "Bizzabo")
    return "Hey {}!".format(name)

@app.route("/webhook", methods=["POST"])
def index():
    project_id = "bizzabo"
    topic_id = "lim-test-topic"
    body = request.data
    logging.warning(body)
    logging.warning("length="+str(len(body)))
    logging.warning("size="+str(getsizeof(body)))
    #add message size in chars and mgb
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    future = publisher.publish(topic_path, body)
    return (future.result())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]