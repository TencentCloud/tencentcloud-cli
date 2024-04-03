**Example 1: 示例**



Input: 

```
tccli live CreateLiveRecordTemplate --cli-unfold-argument  \
    --RemoveWatermark false \
    --FlvParam.StorageTime 2 \
    --FlvParam.VodSubAppId 251195406 \
    --FlvParam.Enable 1 \
    --FlvParam.RecordInterval 2222 \
    --IsDelayLive 0 \
    --Description 字符串 \
    --TemplateName 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "74ed2203-278d-4ec8-8c67-65626a94daef",
        "TemplateId": 362894
    }
}
```

**Example 2: 请求示例**



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

