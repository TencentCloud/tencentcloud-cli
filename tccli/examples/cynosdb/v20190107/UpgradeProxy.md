**Example 1: 升级数据库代理配置**

升级数据库代理配置

Input: 

```
tccli cynosdb UpgradeProxy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-dnofdr2d \
    --ProxyCount 2 \
    --Cpu 2 \
    --Mem 4 \
    --ProxyGroupId cynosdbmysql-proxy-4378e0kb \
    --ReloadBalance auto \
    --IsInMaintainPeriod no \
    --ProxyZones.0.ProxyNodeZone ap-guangzhou-3 \
    --ProxyZones.0.ProxyNodeCount 2
```

Output: 
```
{
    "Response": {
        "FlowId": 127635,
        "TaskId": 174673,
        "RequestId": "a5706353-296a-4992-ad07-ac4a48eeba43"
    }
}
```

