**Example 1: 分析回调事件内容**



Input: 

```
tccli cme ParseEvent --cli-unfold-argument  \
    --Platform test \
    --EventContent {"EventType":"Storage.NewFileCreated","StorageNewFileCreatedEvent":{"FileId":"5285890818667693851","MaterialId":"60a75c1c30fcbe0001cc09d5","Operator":"3fa6b09e-05c6-433e-bc1e-6457d264f1dd","OperationType":"Upload","Owner":{"Type":"PERSON","Id":"3fa6b09e-05c6-433e-bc1e-6457d264f1dd"},"ClassPath":"/媒体"}}
```

Output: 
```
{
    "Response": {
        "EventContent": {
            "EventType": "Storage.NewFileCreated",
            "StorageNewFileCreatedEvent": {
                "FileId": "85890818667698972737",
                "MaterialId": "60a75c1c30fcbe00093ikd93k",
                "Operator": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9",
                "OperationType": "Upload",
                "Owner": {
                    "Type": "PERSON",
                    "Id": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9"
                },
                "ClassPath": "/媒体"
            }
        },
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

