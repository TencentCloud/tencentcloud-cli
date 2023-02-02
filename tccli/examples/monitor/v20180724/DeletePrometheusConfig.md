**Example 1: 删除prometheus配置**

删除prometheus配置

Input: 

```
tccli monitor DeletePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --ClusterType tke \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

