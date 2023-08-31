**Example 1: 获取信息防泄漏规则列表**

获取信息防泄漏规则列表

Input: 

```
tccli waf DescribeAntiInfoLeakageRules --cli-unfold-argument  \
    --Domain xx
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "xx",
        "RuleList": [
            {
                "Status": 1,
                "Name": "xx",
                "RuleId": 1,
                "Uri": "xx",
                "Action": "xx",
                "Strategies": [
                    {
                        "Content": "xx",
                        "Field": "xx",
                        "CompareFunc": "xx"
                    }
                ],
                "CreateTime": "xx"
            }
        ]
    }
}
```

