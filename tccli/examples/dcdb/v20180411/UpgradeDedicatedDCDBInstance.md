**Example 1: 无**



Input: 

```
tccli dcdb UpgradeDedicatedDCDBInstance --cli-unfold-argument  \
    --UpgradeType EXPAND \
    --InstanceId tdsqlshard-jv8z8fhl \
    --ExpandShardConfig.ShardInstanceIds shard-xxx1 shard-xxx2 \
    --ExpandShardConfig.ShardMemory 2 \
    --ExpandShardConfig.ShardStorage 20
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "FlowId": 1122
    }
}
```

