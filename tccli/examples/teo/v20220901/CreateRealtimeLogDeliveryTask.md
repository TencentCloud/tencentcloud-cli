**Example 1: 创建目的地为腾讯云 CLS 的日志投递任务**

创建目的地为腾讯云 CLS 的日志投递任务，投递数据范围为 domain.example.com 在中国大陆境内产生的站点加速日志，包含字段有 RequestID、ClientIP、RequestTime 以及从 Accept-Language 请求头中提取的字段值，配置采样比例为 60.5%。

Input: 

```
tccli teo CreateRealtimeLogDeliveryTask --cli-unfold-argument  \
    --ZoneId zone-xxxxx \
    --TaskName test_log_task \
    --TaskType cls \
    --EntityList domain.example.com \
    --LogType domain \
    --Area mainland \
    --Fields RequestID ClientIP RequestTime \
    --CustomFields.0.Name ReqHeader \
    --CustomFields.0.Value Accept-Language \
    --CustomFields.0.Enabled True \
    --Sample 605 \
    --CLS.LogSetId 1a6efff1-0e40-4d37-a4ed-02c92513406b \
    --CLS.TopicId 0b3a07c0-5cf6-4017-8a75-cd4459aea588 \
    --CLS.LogSetRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "TaskId": "26580056-1187-43ed-b2c7-ecdb5bae0b46",
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a703"
    }
}
```

**Example 2: 创建目的地为自定义 HTTP 服务的日志投递任务**

创建目的地为自定义 HTTP 服务的日志投递任务，投递数据范围为 domain.example.com 在中国大陆境内产生的、请求最终安全处置方式为拦截或挑战的站点加速日志，包含字段有 RequestID、ClientIP、RequestTime，不开启日志采样，开启日志投递压缩，并且在投递日志时携带自定义请求头 Vendor，值固定为 EdgeOne。

Input: 

```
tccli teo CreateRealtimeLogDeliveryTask --cli-unfold-argument  \
    --ZoneId zone-xxxxx \
    --TaskName test_log_task \
    --TaskType custom_endpoint \
    --EntityList domain.example.com \
    --LogType domain \
    --Area mainland \
    --Fields RequestID ClientIP RequestTime \
    --Sample 1000 \
    --DeliveryConditions.0.Conditions.0.Key SecurityAction \
    --DeliveryConditions.0.Conditions.0.Operator equal \
    --DeliveryConditions.0.Conditions.0.Value Deny JSChallenge ManagedChallenge \
    --CustomEndpoint.Url http://custom_endpoint/access_log/post \
    --CustomEndpoint.CompressType gzip \
    --CustomEndpoint.Headers.0.Name Vendor \
    --CustomEndpoint.Headers.0.Value EdgeOne
```

Output: 
```
{
    "Response": {
        "TaskId": "26580056-1187-43ed-b2c7-ecdb5bae0b46",
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a703"
    }
}
```

