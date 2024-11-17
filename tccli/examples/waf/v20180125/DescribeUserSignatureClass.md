**Example 1: 查询Tiga引擎规则类型及状态**

查询Tiga引擎规则类型及状态

Input: 

```
tccli waf DescribeUserSignatureClass --cli-unfold-argument  \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RuleTypeList": [
            {
                "TypeID": "10000000",
                "Name": "rulename",
                "Desc": "description",
                "RuleTypeStatus": 0,
                "ActiveRuleCount": 10,
                "TotalRuleCount": 12
            }
        ],
        "RequestId": "104cf2f9-c733-4a18-8905-372553b6ed80"
    }
}
```

