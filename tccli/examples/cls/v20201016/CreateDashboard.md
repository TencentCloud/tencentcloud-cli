**Example 1: 创建仪表盘**



Input: 

```
tccli cls CreateDashboard --cli-unfold-argument  \
    --DashboardName xx \
    --Data xx \
    --Tags.0.Value xx \
    --Tags.0.Key xx
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

