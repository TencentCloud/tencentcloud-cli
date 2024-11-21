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
                "CVEID": "CVE-2012-6329",
                "IsIgnoreAll": 1,
                "LocalImageCount": 0,
                "PocID": "pcmgr-171244",
                "RegistryImageCount": 0,
                "UpdateTime": "2024-05-21 16:56:04",
                "VulName": "Perl 任意代码执行漏洞（CVE-2012-6329）"
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

