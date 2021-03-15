**Example 1: 获取自定义规则列表**



Input: 

```
tccli waf DescribeCustomRules --cli-unfold-argument  \
    --Domain www.test.com \
    --Edition clb-waf \
    --Paging.Offset 0 \
    --Paging.Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "5d207f4f-0d41-4f5d-bce2-0320090c98d8",
        "RuleList": [
            {
                "ActionType": "1",
                "Bypass": "geoip,cc,owasp,ai,antileakage",
                "CreateTime": "2020-02-20 14:00:12",
                "ExpireTime": "0",
                "Name": "test",
                "Redirect": "/",
                "RuleId": "17958569",
                "SortId": "100",
                "Status": "1",
                "Strategies": [
                    {
                        "Arg": "",
                        "CompareFunc": "ipmatch",
                        "Content": "1.1.1.2",
                        "Field": "IP"
                    }
                ]
            }
        ],
        "TotalCount": "1"
    }
}
```

**Example 2: 带过滤参数返回结果为0的场景**



Input: 

```
tccli waf DescribeCustomRules --cli-unfold-argument  \
    --Domain www.test.com \
    --Edition clb-waf \
    --Paging.Offset 0 \
    --Paging.Limit 10 \
    --Search "1"
```

Output: 
```
{
    "Response": {
        "RequestId": "6d54d3c1-f60b-4766-bf2e-cb29738ed13d",
        "RuleList": [],
        "TotalCount": "0"
    }
}
```

