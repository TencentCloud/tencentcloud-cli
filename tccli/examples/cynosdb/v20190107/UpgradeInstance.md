**Example 1: 实例变配**



Input: 

```
tccli cynosdb UpgradeInstance --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-n7ocdslw \
    --UpgradeType upgradeImmediate \
    --Cpu 2 \
    --Memory 4 \
    --UpgradeProxy.Cpu 4 \
    --UpgradeProxy.Mem 8000 \
    --UpgradeProxy.ReloadBalance auto \
    --UpgradeProxy.ProxyZones.0.ProxyNodeZone ap-guangzhou-3 \
    --UpgradeProxy.ProxyZones.0.ProxyNodeCount 1
```

Output: 
```
{
    "Response": {
        "TranId": "abc",
        "BigDealIds": [
            "abc"
        ],
        "DealNames": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

