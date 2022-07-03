**Example 1: 升级实例**



Input: 

```
tccli cynosdb UpgradeInstance --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-n7ocdslw \
    --UpgradeType upgradeImmediate \
    --Cpu 2 \
    --Memory 4
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

