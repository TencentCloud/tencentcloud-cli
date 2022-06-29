**Example 1: 新增配置**



Input: 

```
tccli tke CreatePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --ClusterType tke \
    --ClusterId cls-xxx \
    --PodMonitor.0.Name xxx \
    --PodMonitor.0.Config xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

