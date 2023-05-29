**Example 1: 升级TDSQL按量计费实例**

升级TDSQL按量计费实例

Input: 

```
tccli dcdb UpgradeHourDCDBInstance --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh \
    --UpgradeType ADD \
    --AddShardConfig.ShardCount 2 \
    --AddShardConfig.ShardMemory 2 \
    --AddShardConfig.ShardStorage 10
```

Output: 
```
{
    "Response": {
        "RequestId": "9b59ee51-0e13-1c2f-dedb-59fabe9d7f4a"
    }
}
```

