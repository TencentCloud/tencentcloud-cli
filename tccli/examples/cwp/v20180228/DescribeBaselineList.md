**Example 1: 查询基线列表接口**

根据过滤参数查询基线列表信息

Input: 

```
tccli cwp DescribeBaselineList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "TotalCount": 100,
        "BaselineList": [
            {
                "Name": "基线名1",
                "Level": 1,
                "RuleCount": 11,
                "HostCount": 12,
                "Status": 0
            },
            {
                "Name": "基线名2",
                "Level": 1,
                "RuleCount": 11,
                "HostCount": 12,
                "Status": 0
            }
        ]
    }
}
```

