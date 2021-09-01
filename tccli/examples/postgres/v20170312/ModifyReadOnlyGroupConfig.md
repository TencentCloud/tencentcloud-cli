**Example 1: 修改只读组配置信息**



Input: 

```
tccli postgres ModifyReadOnlyGroupConfig --cli-unfold-argument  \
    --ReadOnlyGroupId "vpc-e0tfm161" \
    --ReadOnlyGroupName "test" \
    --ReplayLagEliminate 0 \
    --MaxReplayLag 0 \
    --MaxReplayLatency 512 \
    --MinDelayEliminateReserve 0 \
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

