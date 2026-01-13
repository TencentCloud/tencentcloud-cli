**Example 1: 修改仪表盘**

修改仪表盘

Input: 

```
tccli cls ModifyDashboard --cli-unfold-argument  \
    --DashboardId dashboard-e7497a78-667f-45ee-b785-4ac8fca05dc6 \
    --DashboardName 修改仪表盘 \
    --Data {"timezone":"browser","subType":"CLS_Host"} \
    --Tags.0.Value tagValue \
    --Tags.0.Key tagKey
```

Output: 
```
{
    "Response": {
        "RequestId": "73b2ae74-f740-45f9-9202-b40392ad815f"
    }
}
```

