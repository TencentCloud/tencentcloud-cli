**Example 1: 扩容调用成功示例**



Input: 

```
tccli dcdb UpgradeHourDCDBInstance --cli-unfold-argument  \
    --InstanceId tdsqlshard-8q7j1jpih1 \
    --UpgradeType EXPAND \
    --ExpandShardConfig.ShardInstanceIds shard-ezn4l0i8mf \
    --ExpandShardConfig.ShardMemory 2 \
    --ExpandShardConfig.ShardStorage 35 \
    --ExpandShardConfig.ShardNodeCount 2 \
    --SwitchStartTime 2026-08-20 18:00:00 \
    --SwitchEndTime 2026-08-20 18:15:00 \
    --SwitchInterval 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c0748a45-727c-49e1-bdbc-20b5e7fd508e"
    }
}
```

