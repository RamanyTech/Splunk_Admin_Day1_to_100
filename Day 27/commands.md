# Connectivity check from Windows to Indexer

### To enable telnet in Windows:

```bash
dism /online /Enable-Feature /FeatureName:TelnetClient
```

### To check the connectivity
```bash
telnet IP_ADDRESS 9997

```

```bash
Ctrl+]

quit
```
-----------------
# HTTP Event collector - Setup

### HEC_One

```bash 
3457b86f-d279-48a2-b9d7-d273308ce63c
```

```bash
source="http:HEC_One" (index="live9_idx")
```


### HEC_Two
```bash
vi /opt/splunk/etc/apps/search/local/inputs.conf
```
```bash
[http://HEC_Two]
disabled = 0
host = RAMANY-PC
index = live9_idx
indexes = live9_idx,main
sourcetype = http_data
token = 68abd039-ce8a-4b92-a136-38053b45f1da
```

GUID Generator website: https://guidgenerator.com/online-guid-generator.aspx


### HEC_Three
```bash
cd /opt/splunk/bin

./splunk http-event-collector create HEC_Three -uri https://IP_ADDRESS:8089 -description "this is a new token" -disabled 1 -index live9_idx


./splunk http-event-collector enable -name HEC_Three -uri https://IP_ADDRESS:8089 -auth admin:Pa55word
```
--------------------

# HTTP Event collector - Testing

### HEC_One

Run in a Command prompt: - important
```bash
curl -k  http://15.207.161.180:8088/services/collector -H "Authorization:Splunk 3457b86f-d279-48a2-b9d7-d273308ce63c" -d "{\"sourcetype\":  \"trial\",\"event\":\"hello world!\"}"
```

### HEC_Two

Run in a Postman, using below parameters:
```bash
URL --> http://IP_ADDRESS:8088/services/collector

Method --> POST

Headers --> Key = Authorization
			Value = Splunk 3457b86f-d279-48a2-b9d7-d273308ce63c

Body --> raw --> select "JSON" in the dropdown --> enter below text in the text area

{"sourcetype":  "trial","event":"hello my world!"}
```

### HEC_Three

Run in a Python script using below code:

```bash
import requests
import json

url = "http://15.207.161.180:8088/services/collector"

payload = json.dumps({
  "sourcetype": "trial",
  "event": "hello my new world!"
})
headers = {
  'Authorization': 'Splunk 68abd039-ce8a-4b92-a136-38053b45f1da',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
-----------------

# Scripted Input

- Login to Heavy Forwarder

- Switch to splunk user

- Go to below directory
```bash
/opt/splunk/etc/apps/search/bin/
```
- Use below command to download the script
```bash
curl https://raw.githubusercontent.com/RamanyTech/Splunk_Admin_Day1_to_100/refs/heads/main/Day%2027/github-commits.py > github-commits.py
```
- Add permission to make it executable:

```bash
chmod +x github-commits.py
```
------------

- Configurations to be updated in the script:

```bash
OWNER = "OWNER_NAME"  
REPO = "REPO_NAME"   
CHECKPOINT_FILE = "/opt/splunk/etc/apps/search/bin/checkpoint.txt"  
GITHUB_TOKEN = "GTIHUB_TOKEN" 
```
-------------

- Configurations to be kept in inputs.conf
```bash
[script://$SPLUNK_HOME/etc/apps/search/bin/github-commits.py]
disabled = false
host = PROD-RamanyTech
index = live9_idx
interval = 60.0
sourcetype = github_json
```

- Configurations to be kept in props.conf
```bash
[github_json]
SHOULD_LINEMERGE=true
LINE_BREAKER=([\r\n]+)
NO_BINARY_CHECK=true
CHARSET=UTF-8
INDEXED_EXTRACTIONS=json
TIMESTAMP_FIELDS=commit.committer.date
```
