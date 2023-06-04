**Example 1: 获取漏洞库列表**

获取漏洞库列表



Input: 

```
tccli cwp DescribeVulStoreList --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --Limit 0 \
    --Offset 0 \
    --Order abc \
    --By abc
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "VulId": 1,
                "Level": 1,
                "Name": "abc",
                "CveId": "abc",
                "VulCategory": 1,
                "PublishDate": "abc",
                "Method": 1,
                "AttackLevel": 1,
                "FixSwitch": 1,
                "SupportDefense": 1
            }
        ],
        "TotalCount": 1,
        "Remaining": 1,
        "FreeSearchTimes": 1,
        "RequestId": "abc"
    }
}
```

