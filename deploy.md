dDeploying code on GCP
————————————

Extract google-cloud-cli-425.0.0-darwin-x86_64.tar
/Users/ganesh/Downloads/google-cloud-sdk
$ ./gcloud auth login
$ ./gcloud projects list


https://console.cloud.google.com

Create NewProject on console
Name - sampleapplication


Enable — App Engine Admin API — to to be able to build our application in the app engine 
It takes care of all backend compute and gives us UI (no need to worry about infra) .. This is serverless solution

Enable App Engine Admin API to build your application on app engine. —> Takes care of all backend compute, memory etc (All infra). 
A Complete server-less solution on GCP

$ gcloud config set project <poject id displayed in projects list command>
This navigates to your project

App engine -- Dashboard —> Create application
Or command line create — $ gcloud app create

App engine application has been created.
Now we are ready to deploy

Run below in gcloud terminal ..
$ git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
$ cd python-docs-samples/appengine/standard_python3/hello_world

$ gcloud app deploy app.yaml
Once application is deployed —> it gives us an URL.. 

$ gcloud app browse
Go to App Engine —> Dashboard to your application stats

$ gcloud app describe




VM
./gcloud compute ssh --zone "us-east1-b" "demo-vm1" --project "lustrous-oasis-381317"

