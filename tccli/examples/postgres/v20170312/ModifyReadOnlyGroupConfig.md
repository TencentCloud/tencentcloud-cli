**Example 1: 修改只读组配置信息**



Input: 

```
tccli postgres ModifyReadOnlyGroupConfig --cli-unfold-argument  \
    --MaxReplayLag 0 \
    --ReplayLagEliminate 0 \
    --MaxReplayLatency 512 \
    --MinDelayEliminateReserve 0 \
    --ReadOnlyGroupName "test" \
    --ReadOnlyGroupId "vpc-e0tfm161" \
    --Rebalance 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8"
    }
}
```

