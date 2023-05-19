**Example 1: 获取主机安全服务列表**

获取主机安全服务列表

Input: 

```
tccli ssl DescribeHostCosInstanceList --cli-unfold-argument  \
    --ResourceType xx \
    --IsCache 1 \
    --CertificateId xx \
    --Filters.0.FilterKey xx \
    --Filters.0.FilterValue xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AsyncOffset": 0,
        "AsyncTotalNum": 0,
        "InstanceList": [
            {
                "Domain": "hathlim.cn",
                "Status": "ENABLED",
                "CertId": null,
                "Bucket": "hath-1302189209",
                "Region": "ap-nanjing"
            },
            {
                "Domain": "aaa.likeghost.club",
                "Status": "DISABLED",
                "CertId": null,
                "Bucket": "hath-1302189209",
                "Region": "ap-nanjing"
            },
            {
                "Domain": "zz.hathlim.cn",
                "Status": "ENABLED",
                "CertId": null,
                "Bucket": "test-1302189209",
                "Region": "ap-nanjing"
            }
        ],
        "RequestId": "875c1016-64a3-41c3-b3d3-430af1a6e1f9"
    }
}
```

