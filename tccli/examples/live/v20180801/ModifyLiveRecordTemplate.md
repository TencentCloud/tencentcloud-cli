**Example 1: 请求示例**



Input: 

```
tccli live ModifyLiveRecordTemplate --cli-unfold-argument  \
    --TemplateName templat \
    --Description test \
    --FlvParam.Enable 1 \
    --FlvParam.RecordInterval 1800 \
    --FlvParam.StorageTime 700 \
    --TemplateId 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

