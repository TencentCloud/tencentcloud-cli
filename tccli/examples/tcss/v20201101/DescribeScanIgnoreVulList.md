**Example 1: 查询扫描忽略的漏洞列表**



Input: 

```
tccli tcss DescribeScanIgnoreVulList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "IsIgnoreAll": 0,
                "CVEID": "xx",
                "RegistryImageCount": 0,
                "VulName": "xx",
                "UpdateTime": "xx",
                "PocID": "xx",
                "LocalImageCount": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

