**Example 1: 更新监控信息**



Input: 

```
tccli vpc UpdateMonitorInternal --cli-unfold-argument  \
    --UpdateMonitorSet.0.VpcId 1 \
    --UpdateMonitorSet.0.Protocol tcp \
    --UpdateMonitorSet.0.ActiveFlag 0 \
    --UpdateMonitorSet.0.Ip 10.6.2.3 \
    --UpdateMonitorSet.0.Interval 3 \
    --UpdateMonitorSet.0.Port 8181 \
    --UpdateMonitorSet.0.BadLimit 3 \
    --UpdateMonitorSet.0.Timeout 3 \
    --UpdateMonitorSet.0.GroupId 1 \
    --UpdateMonitorSet.0.GoodLimit 3
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

