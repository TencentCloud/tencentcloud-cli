**Example 1: 关闭日志采样功能**

修改某个已经创建成功的实时日志投递任务配置，关闭其日志采样功能。修改前，日志采样比例为 60.5%；修改后，不再进行日志采样，将投递 100% 数量的日志至目的地。

Input: 

```
tccli teo ModifyRealtimeLogDeliveryTask --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnpayol \
    --TaskId 17819248-77b0-4e1a-a979-d84b5a9b300p \
    --Sample 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a703"
    }
}
```

**Example 2: 追加需要投递日志的加速域名**

修改某个已经创建成功的实时日志投递任务配置，为其追加需要投递日志的加速域名。修改前，仅投递 domain1.example.com 的站点加速日志；修改后，将投递 domain1.example.com、domain2.example.com、domain3.example.com 的站点加速日志。

Input: 

```
tccli teo ModifyRealtimeLogDeliveryTask --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnpayol \
    --TaskId 17819248-77b0-4e1a-a979-d84b5a9b300p \
    --EntityList domain1.example.com domain2.example.com domain3.example.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a703"
    }
}
```

