**Example 1: 删除监控信息**



Input: 

```
tccli vpc DeleteMonitorInternal --cli-unfold-argument  \
    --DelMonitorSet.0.Ip 10.6.2.3 \
    --DelMonitorSet.0.VpcId 1 \
    --DelMonitorSet.0.Protocol tcp \
    --DelMonitorSet.0.GroupId 1 \
    --DelMonitorSet.0.Port 8181
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

