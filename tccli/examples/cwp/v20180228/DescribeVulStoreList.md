**Example 1: 获取漏洞库列表**

获取漏洞库列表



Input: 

```
tccli cwp DescribeVulStoreList --cli-unfold-argument  \
    --Filters.0.Name VulName \
    --Filters.0.Values CVE-2023-46604 \
    --Filters.0.ExactMatch True \
    --Limit 10 \
    --Offset 0 \
    --Order DESC \
    --By PublishDate
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "VulId": 105006,
                "Level": 4,
                "Name": "Apache ActiveMQ远程代码执行漏洞(CVE-2023-46604)",
                "CveId": "CVE-2023-46604",
                "VulCategory": 2,
                "PublishDate": "2023-10-24 00:00:00",
                "Method": 0,
                "AttackLevel": 3,
                "FixSwitch": 0,
                "SupportDefense": 1
            }
        ],
        "TotalCount": 1,
        "Remaining": 1,
        "FreeSearchTimes": 1,
        "RequestId": "e5b4724c-49af-46ab-bd84-cdbae897e7e0"
    }
}
```

