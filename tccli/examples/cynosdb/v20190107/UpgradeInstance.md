**Example 1: 实例变配**



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

