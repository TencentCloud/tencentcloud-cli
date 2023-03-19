**Example 1: 修改仪表盘**

修改仪表盘

Input: 

```
tccli cls ModifyDashboard --cli-unfold-argument  \
    --DashboardId dashboard-x-x-x-x \
    --DashboardName 修改仪表盘 \
    --Data {} \
    --Tags.0.Value tagValue \
    --Tags.0.Key tagKey
```

Output: 
```
{
    "Response": {
        "RequestId": "xx-xx-xx-xx"
    }
}
```

