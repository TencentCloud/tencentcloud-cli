**Example 1: 删除采集配置**



Input: 

```
tccli tke DeletePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-2tghe0lv \
    --ClusterId cls-9cgtidkr \
    --ClusterType tke
```

Output: 
```
{
    "Response": {
        "RequestId": "254f0ea8-6b2c-44f7-913e-74fb6d62255b"
    }
}
```

**Example 2: 删除prometheus采集配置**



Input: 

```
tccli tke DeletePrometheusConfig --cli-unfold-argument  \
    --InstanceId abc \
    --ClusterType abc \
    --ClusterId abc \
    --ServiceMonitors abc \
    --PodMonitors abc \
    --RawJobs abc \
    --Probes abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

