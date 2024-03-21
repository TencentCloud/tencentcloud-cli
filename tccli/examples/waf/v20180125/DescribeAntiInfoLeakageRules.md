**Example 1: 获取信息防泄漏规则列表**

获取信息防泄漏规则列表

Input: 

```
tccli waf DescribeAntiInfoLeakageRules --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Order Desc \
    --Limit 1 \
    --Filters.0.Values 0 \
    --Filters.0.Name Action \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "66ec4266-fce2-4238-bb69-8b99f3b19ad0",
        "RuleList": [
            {
                "Status": 1,
                "Name": "RuleName",
                "RuleId": 1,
                "Uri": "/url",
                "Action": "0",
                "Strategies": [
                    {
                        "Content": "",
                        "Field": "information",
                        "CompareFunc": "contains"
                    }
                ],
                "CreateTime": "2022-10-26T16:31:43+08:00"
            }
        ]
    }
}
```

