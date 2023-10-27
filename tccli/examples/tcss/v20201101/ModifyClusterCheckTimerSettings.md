**Example 1: 修改集群检查定时设置**

修改集群检查定时设置

Input: 

```
tccli tcss ModifyClusterCheckTimerSettings --cli-unfold-argument  \
    --Status True \
    --ClusterIDs abc \
    --CycleDay 1 \
    --ScanTimeBegin abc \
    --ScanTimeEnd abc \
    --ScanScope 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

