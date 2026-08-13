**Example 1: 查询edr告警的多攻击阶段**



Input: 

```
tccli csip DescribeEdrAlertMultiAttackStages --cli-unfold-argument  \
    --Targets.0.Id 1000000000025741 \
    --Targets.0.AppId 260146618 \
    --Targets.0.AlertId c2717afac6a8f6004a108d0ef9702b7f \
    --Targets.0.Quuid 8ceae791-925f-4a77-be58-22e9f7ead617 \
    --Targets.0.InstanceId ins-f1vbqysn \
    --Targets.0.AlertSubType MULTI_BEHAVIOR_ATTACK
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "b2f45cfe-359b-4712-93ab-3b00ddb89079"
    }
}
```

