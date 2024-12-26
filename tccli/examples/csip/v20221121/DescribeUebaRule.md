**Example 1: test**



Input: 

```
tccli csip DescribeUebaRule --cli-unfold-argument  \
    --Filter.Filters.0.Name RuleType \
    --Filter.Filters.0.Values 0 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --MemberId mem-e5d75d512c934d2c
```

Output: 
```
{
    "Response": {
        "AlterType": [
            {
                "Text": "用户异常行为",
                "Value": "AbnormalUserBehavior"
            }
        ],
        "Data": [
            {
                "RuleID": "rule-k23p01f",
                "RuleName": "11",
                "RuleType": 1,
                "RuleLevel": 4,
                "RuleContent": "用户类型: 云用户  日志类型: AWS日志(云审计)\n逻辑表达式: (account_id 等于 10) \n统计条件:不基于统计检测",
                "RuleStatus": true,
                "HitCount": 0,
                "AppID": "79254734186",
                "Uin": "arn:aws-cn:iam::792***4186:user/TC_20240510_nZFQ",
                "MemberID": "mem-aws-b****e82cb251dd",
                "Nickname": "TC_20240510_nZFQ",
                "CloudType": 0,
                "CustomRuleDetail": {
                    "RuleName": "11",
                    "UserType": 1,
                    "LogType": "8_3",
                    "LogTypeStr": "AWS日志(云审计)",
                    "TimeInterval": 1,
                    "EventContent": {
                        "EventType": 2,
                        "Content": "zero**",
                        "Filters": [
                            {
                                "Name": "account_id",
                                "Values": [
                                    "10"
                                ],
                                "OperatorType": 0
                            }
                        ]
                    },
                    "AlertName": "AbnormalUserBehavior",
                    "AlterLevel": 4,
                    "Operator": [
                        "account_id",
                        "action_type"
                    ],
                    "OperateObject": [
                        "account_id"
                    ],
                    "OperateMethod": [
                        "account_id"
                    ]
                }
            }
        ],
        "RequestId": "7da0af7a-c1c7-4739-8961-1492d37d693a",
        "TotalCount": 76
    }
}
```

