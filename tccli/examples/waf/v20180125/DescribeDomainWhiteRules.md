**Example 1: 获取域名的规则白名单**

获取域名的规则白名单

Input: 

```
tccli waf DescribeDomainWhiteRules --cli-unfold-argument  \
    --Domain test.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "RuleList": [
            {
                "Id": 1,
                "Rules": [
                    2,
                    3,
                    4
                ],
                "Url": "/test",
                "Function": "eq",
                "Time": "2020-08-20 00:00:00",
                "Status": 1
            }
        ]
    }
}
```

