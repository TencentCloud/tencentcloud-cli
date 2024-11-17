**Example 1: 获取用户特征规则列表**

获取用户特征规则列表

Input: 

```
tccli waf DescribeUserSignatureRuleV2 --cli-unfold-argument  \
    --Domain abc \
    --Offset 1 \
    --Limit 1 \
    --By abc \
    --Order abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Rules": [
            {
                "ID": "0100000",
                "Status": 0,
                "MainClassID": "02000000",
                "SubClassID": "02200000",
                "CveID": "cve-111111",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "MainClassName": "xss",
                "SubClassName": "xss-1",
                "Description": "",
                "Reason": 0,
                "RiskLevel": 1
            }
        ],
        "RequestId": "xxxx-aaaa-ddd"
    }
}
```

