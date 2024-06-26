**Example 1: 新增配置**



Input: 

```
tccli tke ModifyPrometheusConfig --cli-unfold-argument  \
    --InstanceId abc \
    --ClusterType abc \
    --ClusterId abc \
    --ServiceMonitors.0.Name abc \
    --ServiceMonitors.0.Config abc \
    --ServiceMonitors.0.TemplateId abc \
    --PodMonitors.0.Name abc \
    --PodMonitors.0.Config abc \
    --PodMonitors.0.TemplateId abc \
    --RawJobs.0.Name abc \
    --RawJobs.0.Config abc \
    --RawJobs.0.TemplateId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

**Example 2: 修改采集配置**



Input: 

```
tccli tke ModifyPrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-2tghe0lv \
    --ClusterId cls-9cgtidkr \
    --ClusterType tke
```

Output: 
```
{
    "Response": {
        "RequestId": "f4ae1102-75e5-4eec-900a-2cfe9da33068"
    }
}
```

