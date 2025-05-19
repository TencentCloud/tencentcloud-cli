**Example 1: 新增配置**



Input: 

```
tccli tke CreatePrometheusConfig --cli-unfold-argument  \
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
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 创建采集配置**



Input: 

```
tccli tke CreatePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-2tghe0lv \
    --ClusterId cls-9cgtidkr \
    --ClusterType tke
```

Output: 
```
{
    "Response": {
        "RequestId": "70efa2de-4a2b-4c64-8c13-b87d013f7b9d"
    }
}
```

