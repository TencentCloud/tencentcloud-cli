**Example 1: 修改主机监控采集配置**



Input: 

```
tccli cls ModifyHostMetricConfig --cli-unfold-argument  \
    --TopicId 46c21ba9-b6ea-45f1-8710-5ad92b978b7a \
    --ConfigId b64d4365-0d37-4db0-a603-1412e8bb747c \
    --Name metric_config_update \
    --Interval 35000
```

Output: 
```
{
    "Response": {
        "RequestId": "12b800c1-123c-4148-8d16-bc816dc71ecc"
    }
}
```

