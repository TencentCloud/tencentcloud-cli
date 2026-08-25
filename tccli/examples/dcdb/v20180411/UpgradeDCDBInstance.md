**Example 1: 分布式垂直扩容示例**



Input: 

```
tccli dcdb UpgradeDCDBInstance --cli-unfold-argument  \
    --InstanceId tdsqlshard-8q7j1jpih1 \
    --UpgradeType EXPAND \
    --ExpandShardConfig.ShardInstanceIds shard-ezn4l0i8mf \
    --ExpandShardConfig.ShardMemory 2 \
    --ExpandShardConfig.ShardStorage 20 \
    --ExpandShardConfig.ShardNodeCount 2 \
    --SwitchStartTime 2026-08-20 18:00:00 \
    --SwitchEndTime 2026-08-20 18:15:00 \
    --SwitchInterval 1
```

Output: 
```
{
    "Response": {
        "DealName": "20260820013023408391271",
        "RequestId": "01f590d7-6046-4625-b4ac-b72ed110aeff"
    }
}
```

