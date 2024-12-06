**Example 1: 获取CDN证书部署域名列表**

获取CDN证书部署域名列表

Input: 

```
tccli ssl DescribeHostCdnInstanceList --cli-unfold-argument  \
    --CertificateId hhj****k \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --ResourceType cdn \
    --OldCertificateId yey***j \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "www.zrh.com",
                "CertId": "gss***kl",
                "Status": "normal",
                "HttpsBillingSwitch": "1"
            }
        ],
        "TotalCount": 1,
        "AsyncTotalNum": 0,
        "AsyncOffset": 0,
        "AsyncCacheTime": "2023-10-12 12:00:00",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

