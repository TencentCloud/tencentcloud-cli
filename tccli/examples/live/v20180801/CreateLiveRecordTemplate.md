**Example 1: 请求示例**



Input: 

```
tccli live CreateLiveRecordTemplate --cli-unfold-argument  \
    --TemplateName templat \
    --Description test \
    --FlvParam.Enable 0 \
    --FlvParam.RecordInterval 1800 \
    --FlvParam.StorageTime 600 \
    --HlsParam.Enable 1 \
    --HlsParam.RecordInterval 1800 \
    --HlsParam.StorageTime 600
```

Output: 
```
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

