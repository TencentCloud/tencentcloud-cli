**Example 1: 升级实例**



Input: 

```
tccli cynosdb UpgradeInstance --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-n7ocdslw \
    --Cpu 2 \
    --Memory 4 \
    --UpgradeType upgradeImmediate
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "xx"
        ],
        "RequestId": "165202",
        "TranId": "xx",
        "DealNames": [
            "xx"
        ]
    }
}
```

