**Example 1: Sample request**



Input: 

```
tccli live DescribeLiveRecordTemplate --cli-unfold-argument  \
    --TemplateId 10000
```

Output: 
```
{
    "Response": {
        "Template": {
            "TemplateID": 1000,
            "TemplateName": "testName",
            "Description": "test",
            "FlvParam": {
                "Enable": 1,
                "RecordInterval": 1800,
                "StorageTime": 600
            },
            "HlsParam": {
                "Enable": 0,
                "RecordInterval": 1800,
                "StorageTime": 600
            },
            "IsDelayLive": 0,
            "HlsSpecialParam": {
                "FlowContinueDuration": 60
            }
        },
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

