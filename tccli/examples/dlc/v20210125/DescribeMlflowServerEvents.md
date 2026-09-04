**Example 1: 查询 MlFlow Server K8s 事件**



Input: 

```
tccli dlc DescribeMlflowServerEvents --cli-unfold-argument  \
    --ServerId mlflow-7f72b80b \
    --EventType Normal \
    --PageSize 3
```

Output: 
```
{
    "Response": {
        "Context": "Y29udGV4dC1iNTk4ODcwNS05MmNkLTRhYmEtYmI0MC1lNGQzOGZlYjExODQxNzg1OTM2MzQ5NjUw",
        "EndTime": 1785936349184,
        "Events": [
            {
                "Component": "Pod",
                "EventTime": 1785931379000,
                "InvolvedObjectName": "mlflow-7f72b80b-mlflow-server-7b8b8b5486-85thx",
                "Level": "Normal",
                "Message": "{\"namespace\":\"dlc-p-axzbtgug\",\"name\":\"mlflow-7f72b80b-mlflow-server-7b8b8b5486-85thx\",\"podIP\":\"30.0.2.11\",\"scheduledTime\":\"2026-08-05T20:01:37+08:00\",\"setDuration\":\"1m21s\",\"assignedDuration\":\"1m20s\",\"cniTypes\":[\"tke-route-eni\"],\"staticMode\":true,\"staticIP\":false,\"nodeType\":\"Normal\",\"podUID\":\"4b3cae38-9c0f-4cbb-a809-d2593c021db2\"}",
                "Reason": "SucceedSetPodIP",
                "SourceComponent": "tke-eni-ipamd"
            }
        ],
        "ListOver": false,
        "StartTime": 1785849949184,
        "RequestId": "2dfd613d-7553-4c5e-b550-32a9cdc5b91d"
    }
}
```

