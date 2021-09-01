**Example 1: 创建grafana面板**



Input: 

```
tccli tke CreatePrometheusDashboard --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --DashboardName test-dashboards \
    --Contens test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

