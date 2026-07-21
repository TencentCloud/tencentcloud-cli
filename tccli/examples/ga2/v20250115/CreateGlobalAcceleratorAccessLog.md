**Example 1: 创建访问日志示例**



Input: 

```
tccli ga2 CreateGlobalAcceleratorAccessLog --cli-unfold-argument  \
    --GlobalAcceleratorId ga-8sreohed \
    --ListenerId lsr-4afw0c06 \
    --EndpointGroupId epg-du8oqpy5 \
    --CloudRegion ap-guangzhou \
    --CloudLogId 61f7ee4c-4704-4669-82fe-2c191f8f200b \
    --CloudLogSetId 81217ea2-f578-451a-946e-f31e2131a9ac \
    --FieldKeys request_method \
    --FlowLogDescription ga_log_test_http
```

Output: 
```
{
    "Response": {
        "LogPushTaskId": "galog-gv9duwet",
        "RequestId": "383fea40-a621-4bb6-8695-ad35e26515c2"
    }
}
```

