**Example 1: 创建仪表盘**

创建仪表盘

Input: 

```
tccli cls CreateDashboard --cli-unfold-argument  \
    --DashboardName 仪表盘名称 \
    --Data {} \
    --Tags.0.Value tagValue \
    --Tags.0.Key tagKey
```

Output: 
```
{
    "Response": {
        "DashboardId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

