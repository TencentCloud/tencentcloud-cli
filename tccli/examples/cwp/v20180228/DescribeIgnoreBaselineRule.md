**Example 1: 查询忽略检测项信息**

查询已经进行忽略操作的检测项信息

Input: 

```
tccli cwp DescribeIgnoreBaselineRule --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --RuleName test
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100,
        "IgnoreBaselineRuleList": [
            {
                "RuleName": "检测项1",
                "RuleId": 1,
                "EffectHostCount": 20,
                "ModifyTime": "2020-11-11 :00:00:00",
                "Fix": "重启"
            },
            {
                "RuleName": "检测项2",
                "EffectHostCount": 25,
                "RuleId": 12,
                "ModifyTime": "2020-11-11 :00:00:50",
                "Fix": "重启2次"
            }
        ]
    }
}
```

