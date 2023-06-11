**Example 1: 获取CDN证书部署域名列表**

获取CDN证书部署域名列表

Input: 

```
tccli ssl DescribeHostCdnInstanceList --cli-unfold-argument  \
    --CertificateId abc \
    --IsCache 1 \
    --Filters.0.FilterKey abc \
    --Filters.0.FilterValue abc \
    --ResourceType abc \
    --OldCertificateId abc \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "abc",
                "CertId": "abc",
                "Status": "abc"
            }
        ],
        "TotalCount": 1,
        "AsyncTotalNum": 0,
        "AsyncOffset": 0,
        "AsyncCacheTime": "abc",
        "RequestId": "abc"
    }
}
```

