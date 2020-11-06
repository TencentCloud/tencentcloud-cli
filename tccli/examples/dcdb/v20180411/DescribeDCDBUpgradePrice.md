**Example 1: 查询升级分布式数据库实例的价格**



Input: 

```
tccli dcdb DescribeDCDBUpgradePrice --cli-unfold-argument  \
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
        "RequestId": "7212a9ec-a235-2144-98d4-59fbe6f14d79",
        "OriginalPrice": 7020,
        "Price": 7020
    }
}
```

