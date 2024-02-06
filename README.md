# bq-python-example
This is to test the data analysis infrastructure.

## Execute the example.
```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates gnupg curl sudo
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-cli
gcloud init
cd example/
pip3 install google-cloud-bigquery
gcloud config set project inunaki
gcloud auth application-default login
python query_bigquery.py
```

## reference
- [gcloud](https://cloud.google.com/sdk/docs/install-sdk?hl=ja#deb)
