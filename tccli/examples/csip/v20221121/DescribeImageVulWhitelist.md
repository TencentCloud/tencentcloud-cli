**Example 1: 查询容器镜像漏洞白名单**



Input: 

```
tccli csip DescribeImageVulWhitelist --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "WhiteList": [
            {
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "PocId": "tvd736",
                "Remark": "漏洞白名单",
                "RuleId": 1,
                "Scope": 1,
                "VulName": " Oracle MySQL Server 安全漏洞 (CVE-2017-3600)"
            }
        ],
        "RequestId": "4c833cf5-50cb-42b0-9028-bfcdc9656215"
    }
}
```

