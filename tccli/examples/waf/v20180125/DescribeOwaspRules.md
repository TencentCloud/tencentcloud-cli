**Example 1: 展示规则**



Input: 

```
tccli waf DescribeOwaspRules --cli-unfold-argument  \
    --Domain owasp.saas3.testwaf.com \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CreateTime": "2021-10-12T17:12:40+08:00",
                "CveID": "",
                "Description": "防护 eval、phpinfo 等 asp、php 代码执行或者 webshell 上传特征",
                "Level": 200,
                "Locked": 1,
                "Reason": 0,
                "RuleId": 16,
                "Status": 1,
                "TypeId": 10000000,
                "VulLevel": 0
            }
        ],
        "RequestId": "03e5562c-d809-4435-8bb5-2c1438b943b3",
        "Total": 1320
    }
}
```

