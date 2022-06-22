**Example 1: 创建只读组**



Input: 

```
tccli postgres CreateReadOnlyGroup --cli-unfold-argument  \
    --MaxReplayLag 0 \
    --VpcId "vpc-e0tfm161" \
    --Name "test" \
    --ProjectId 0 \
    --MasterDBInstanceId "postgres-k95qzetn" \
    --MinDelayEliminateReserve 0 \
    --ReplayLagEliminate 0 \
    --SubnetId "subnet-443a3lv6"
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

