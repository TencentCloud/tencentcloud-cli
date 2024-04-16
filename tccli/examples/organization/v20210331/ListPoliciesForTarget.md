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
                "StrategyId": 134173928,
                "StrategyName": "policy-test-1",
                "AddTime": "2022-08-07 20:20:09",
                "UpdateTime": "2022-08-07 20:20:09",
                "AttachTime": "2022-08-08 14:49:59",
                "Type": 2,
                "Remark": "test1",
                "Uin": 111111111111,
                "Name": "test"
            },
            {
                "StrategyId": 1000,
                "StrategyName": "FullQcloudAccess",
                "AddTime": "2022-08-08 14:45:50",
                "UpdateTime": "2022-08-08 14:49:59",
                "AttachTime": "2022-08-08 14:49:59",
                "Type": 2,
                "Remark": "允许授权所有操作，用于企业组织服务控制策略。",
                "Uin": 111111111111,
                "Name": "test"
            }
        ],
        "TotalNum": 2,
        "RequestId": "2f76e3a5-225f-4deb-8d98-4efb0f1ae0ea"
    }
}
```

