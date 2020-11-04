**Example 1: 升级实例**



Input: 

```
tccli cynosdb UpgradeInstance --cli-unfold-argument  \
    --InstanceId cynosdbpg-ins-n7ocdslw\
    --Cpu 2\
    --Memory 4\
    --UpgradeType upgradeImmediate
```

Output: 
```
{
    "Response": {
        "RequestId": "165202",
        "TaskId": "1021"
    }
}
```

