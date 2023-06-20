**Example 1: 升级数据库代理配置**

升级数据库代理配置

Input: 

```
tccli cynosdb UpgradeProxy --cli-unfold-argument  \
    --ClusterId abc \
    --ProxyCount 0 \
    --Cpu 0 \
    --Mem 0 \
    --ProxyGroupId abc \
    --ReloadBalance abc \
    --IsInMaintainPeriod abc \
    --ProxyZones.0.ProxyNodeZone abc \
    --ProxyZones.0.ProxyNodeCount 0
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "TaskId": 0,
        "RequestId": "abc"
    }
}
```

