**Example 1: 创建一个模板**



Input: 

```
tccli tke CreatePrometheusTemp --cli-unfold-argument  \
    --Template.Name t1 \
    --Template.Describe 一个模板 \
    --Template.ServiceMonitors.0.Name s \
    --Template.ServiceMonitors.0.Config xx \
    --Template.Level cluster
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TemplateId": "temp-xxx"
    }
}
```

