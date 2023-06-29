**Example 1: TbaseV2后付费创建实例**



Input: 

```
tccli tbase CreateInstanceHour --cli-unfold-argument  \
    --DnNode.NodeCount 0 \
    --DnNode.SyncType xx \
    --DnNode.Storage 0 \
    --DnNode.SetCount 0 \
    --DnNode.SpecCode xx \
    --VpcId xx \
    --Zone xx \
    --GoodsNum 0 \
    --AdminPassword xx \
    --Recovery.RecoveryInstanceId xx \
    --Recovery.RecoveryTime xx \
    --Recovery.RecoveryTimePoint xx \
    --Recovery.RecoveryTaskId 0 \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --NetType xx \
    --EngineVersion xx \
    --SubnetId xx \
    --CnNode.NodeCount 0 \
    --CnNode.SyncType xx \
    --CnNode.Storage 0 \
    --CnNode.SetCount 0 \
    --CnNode.SpecCode xx \
    --Charset xx \
    --InstanceName xx \
    --SecurityGroupIdList xx
```

Output: 
```
{
    "Response": {
        "TaskId": 0,
        "InstanceIds": [
            "xx"
        ],
        "BillId": "xx",
        "RequestId": "xx"
    }
}
```

