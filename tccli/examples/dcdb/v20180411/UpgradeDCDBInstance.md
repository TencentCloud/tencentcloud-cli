**Example 1: 升级分布式数据库**



Input: 

```
tccli dcdb UpgradeDCDBInstance --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh \
    --UpgradeType ADD \
    --AddShardConfig.ShardCount 2 \
    --AddShardConfig.ShardMemory 2 \
    --AddShardConfig.ShardStorage 10 \
    --AutoVoucher false
```

Output: 
```
{
    "Response": {
        "RequestId": "9b59ee51-0e13-1c2f-dedb-59fabe9d7f4a",
        "DealName": "20180103110035"
    }
}
```

