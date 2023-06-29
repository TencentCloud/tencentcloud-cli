**Example 1: 查询边缘集群监控状态1**



Input: 

```
tccli iecp DescribeEdgeUnitMonitorStatus --cli-unfold-argument  \
    --EdgeUnitId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "21eaa108-8ffd-40a9-ad01-9272799baf8e",
        "MonitorStatus": "running",
        "IsAvailable": true
    }
}
```

**Example 2: 查询边缘集群监控状态2**



Input: 

```
tccli iecp DescribeEdgeUnitMonitorStatus --cli-unfold-argument  \
    --EdgeUnitId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "21eaa108-8ffd-40a9-ad01-9272799baf8e",
        "MonitorStatus": "deploying",
        "IsAvailable": false
    }
}
```

