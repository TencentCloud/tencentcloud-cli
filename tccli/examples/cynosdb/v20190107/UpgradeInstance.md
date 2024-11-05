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
        "BigDealIds": [],
        "DealNames": [
            "20241025054071351304161"
        ],
        "RequestId": "588fbc90-61a4-4125-bc70-65a3f8d1327e",
        "TranId": "20241025054071351304171"
    }
}
```

