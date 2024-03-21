**Example 1: 获取信息防泄漏规则列表**

获取信息防泄漏规则列表

Input: 

```
tccli waf DescribeAntiInfoLeakRules --cli-unfold-argument  \
    --Domain abc \
    --ActionType 0 \
    --PageInfo.PageNumber abc \
    --PageInfo.PageSize abc
```

Output: 
```
{
    "Response": {
        "TotalCount": "abc",
        "RuleList": [
            {
                "RuleId": "abc",
                "Name": "abc",
                "Status": "abc",
                "ActionType": "abc",
                "CreateTime": "abc",
                "Strategies": [
                    {
                        "Field": "abc",
                        "CompareFunc": "abc",
                        "Content": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

