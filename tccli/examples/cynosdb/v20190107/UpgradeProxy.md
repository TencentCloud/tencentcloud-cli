**Example 1: 升级数据库代理配置**

升级数据库代理配置

Input: 

```
tccli cynosdb UpgradeProxy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-abc \
    --ProxyCount 2 \
    --Cpu 2 \
    --Mem 4 \
    --ProxyGroupId cynosdbmysql-node-asd \
    --ReloadBalance auto \
    --IsInMaintainPeriod no \
    --ProxyZones.0.ProxyNodeZone ap-guangzhou-3 \
    --ProxyZones.0.ProxyNodeCount 2
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

