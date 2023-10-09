**Example 1: 网络攻击数据统计**

网络攻击数据统计

Input: 

```
tccli cwp DescribeAttackStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AttackSrcIpCount": 3,
        "AttackedAssetCount": 0,
        "AttackedPortCount": 1,
        "NewAttackSrcIpCount": 3,
        "NewAttackedAssetCount": 0,
        "NewAttackedPortCount": 1,
        "PendingAttackCount": 3,
        "PendingNewAttackCount": 3,
        "PendingSuccAttackCount": 0,
        "PendingTryAttackCount": 3,
        "RequestId": "619097e1-820e-47f7-b374-187debd09311"
    }
}
```

