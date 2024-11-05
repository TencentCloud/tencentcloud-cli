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
        "RequestId": "f1dd9f5e-4ac0-48a7-9410-c86d24656d9a",
        "TotalCount": 2,
        "BaselineList": [
            {
                "Name": "基线名1",
                "Level": 1,
                "RuleCount": 11,
                "HostCount": 12,
                "Status": 0,
                "CategoryId": 2,
                "LastScanTime": "2024-11-04 03:43:26",
                "MaxStatus": 2,
                "BaselineFailCount": 29
            }
        ]
    }
}
```

