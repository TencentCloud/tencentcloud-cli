**Example 1: 调用成功示例**



Input: 

```
tccli dcdb UpgradeDedicatedDCDBInstance --cli-unfold-argument  \
    --UpgradeType EXPAND \
    --InstanceId tdsqlshard-f2jujx9wap \
    --ExpandShardConfig.ShardInstanceIds shard-5lfxfz1z3f \
    --ExpandShardConfig.ShardMemory 2 \
    --ExpandShardConfig.ShardStorage 10 \
    --SwitchStartTime 2026-08-24 22:00:00 \
    --SwitchEndTime 2026-08-24 22:15:00 \
    --SwitchInterval 5
```

Output: 
```
{
    "Response": {
        "FlowId": 75,
        "RequestId": "d7dca4f8-43c2-4608-8f00-25afcdb18521"
    }
}
```

