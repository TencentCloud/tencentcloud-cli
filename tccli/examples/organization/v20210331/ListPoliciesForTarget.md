**Example 1: 查询目标关联的策略列表**

查询目标关联的策略列表

Input: 

```
tccli organization ListPoliciesForTarget --cli-unfold-argument  \
    --TargetId 111111111111
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "StrategyId": 10001,
                "StrategyName": "policy_name",
                "AddTime": "2022-08-07 20:20:09",
                "UpdateTime": "2022-08-07 20:20:09",
                "AttachTime": "2022-08-08 14:49:59",
                "Type": 2,
                "Remark": "deny policy",
                "Uin": 111111111111,
                "Name": "member_name"
            }
        ],
        "TotalNum": 1,
        "RequestId": "2f76e3a5-225f-4deb-8d98-4efb0f1ae0ea"
    }
}
```

