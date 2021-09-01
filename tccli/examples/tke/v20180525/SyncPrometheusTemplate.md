**Example 1: 同步模板到实例**



Input: 

```
tccli tke SyncPrometheusTemplate --cli-unfold-argument  \
    --TemplateId "temp-xxx" \
    --Targets.0.Region "ap-shanghai" \
    --Targets.0.InstanceId "prom-xxx"
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

