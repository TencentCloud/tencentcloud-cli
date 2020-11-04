**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveRecordTemplates --cli-unfold-argument  \
    --IsDelayLive 1
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": 1000,
                "TemplateName": "testName",
                "IsDelayLive": 1,
                "Description": "test",
                "FlvParam": {
                    "Enable": 0,
                    "RecordInterval": 1800,
                    "StorageTime": 6000,
                    "VodSubAppId": 123456
                },
                "HlsParam": {
                    "Enable": 1,
                    "RecordInterval": 1800,
                    "StorageTime": 600,
                    "VodSubAppId": 123456
                },
                "HlsSpecialParam": {
                    "FlowContinueDuration": 60
                }
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

