**Example 1: 添加更新监控信息**



Input: 

```
tccli vpc CreateUpdateMonitorInternal --cli-unfold-argument  \
    --AddUpdateMonitorSet.0.VpcId 1 \
    --AddUpdateMonitorSet.0.Protocol tcp \
    --AddUpdateMonitorSet.0.ActiveFlag 0 \
    --AddUpdateMonitorSet.0.Ip 10.6.2.3 \
    --AddUpdateMonitorSet.0.Interval 3 \
    --AddUpdateMonitorSet.0.Port 8181 \
    --AddUpdateMonitorSet.0.BadLimit 3 \
    --AddUpdateMonitorSet.0.Timeout 3 \
    --AddUpdateMonitorSet.0.GroupId 1 \
    --AddUpdateMonitorSet.0.GoodLimit 3
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

