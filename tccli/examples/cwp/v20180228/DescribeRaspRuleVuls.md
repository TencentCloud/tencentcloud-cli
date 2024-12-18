**Example 1: 获取漏洞防御白名单漏洞列表**

获取漏洞防御白名单漏洞列表

Input: 

```
tccli cwp DescribeRaspRuleVuls --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name WhiteType \
    --Filters.0.Values 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CveID": "CVE-2012-4453",
                "SupportDefense": 2,
                "VulVulsID": 1,
                "VulVulsName": "dracut 权限许可和访问控制漏洞 (CVE-2012-4453)"
            }
        ],
        "RequestId": "30738e90-7f04-4196-8872-84d27ba02c45",
        "TotalCount": 1
    }
}
```

