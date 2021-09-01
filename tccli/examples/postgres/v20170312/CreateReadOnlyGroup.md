**Example 1: 创建只读组**



Input: 

```
tccli postgres CreateReadOnlyGroup --cli-unfold-argument  \
    --ProjectId 0 \
    --VpcId "vpc-e0tfm161" \
    --SubnetId "subnet-443a3lv6" \
    --MasterDBInstanceId "postgres-k95qzetn" \
    --Name "test" \
    --ReplayLagEliminate 0 \
    --MaxReplayLag 0 \
    --MinDelayEliminateReserve 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8",
        "FlowId": 912,
        "ReadOnlyGroupId": "pgrogrp-dh6873gz"
    }
}
```

