**Example 1: 添加监控信息**



Input: 

```
tccli vpc CreateMonitorInternal --cli-unfold-argument  \
    --AddMonitorSet.0.VpcId 1 \
    --AddMonitorSet.0.Protocol tcp \
    --AddMonitorSet.0.ActiveFlag 0 \
    --AddMonitorSet.0.Ip 10.6.2.3 \
    --AddMonitorSet.0.Interval 3 \
    --AddMonitorSet.0.Port 8181 \
    --AddMonitorSet.0.BadLimit 3 \
    --AddMonitorSet.0.Timeout 3 \
    --AddMonitorSet.0.GroupId 1 \
    --AddMonitorSet.0.GoodLimit 3
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

