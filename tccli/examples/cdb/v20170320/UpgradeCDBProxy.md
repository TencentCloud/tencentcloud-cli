**Example 1: 升级数据库代理配置**



Input: 

```
tccli cdb UpgradeCDBProxy --cli-unfold-argument  \
    --UpgradeTime nowTime \
    --ProxyGroupId proxy-test \
    --InstanceId cdb-test \
    --Mem 4000 \
    --ReloadBalance true \
    --Cpu 2 \
    --ProxyCount 4
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "8155d27a-079a2580-19593e48-f1af5042",
        "RequestId": "3689c0eb-a92d-77ce-0ee2-17d99f604e64"
    }
}
```

