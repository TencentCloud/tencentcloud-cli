**Example 1: 升级数据库代理版本**



Input: 

```
tccli cdb UpgradeCDBProxyVersion --cli-unfold-argument  \
    --InstanceId cdb-test \
    --ProxyGroupId proxy-test \
    --DstProxyVersion 1.0.1 \
    --SrcProxyVersion 1.1.2 \
    --UpgradeTime nowTime
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

