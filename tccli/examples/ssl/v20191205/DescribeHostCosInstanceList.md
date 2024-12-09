**Example 1: 证书部署COS实例列表**

证书部署COS实例列表

Input: 

```
tccli ssl DescribeHostCosInstanceList --cli-unfold-argument  \
    --CertificateId Hhh**kk \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --ResourceType clb
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "www.test.com",
                "CertId": "Hhh**kk",
                "Status": "ENABLED",
                "Bucket": "1873sjejej**kdkdk.cos",
                "Region": "ap-guangzhou"
            }
        ],
        "TotalCount": 1,
        "AsyncTotalNum": 0,
        "AsyncOffset": 0,
        "AsyncCacheTime": "2023-01-24 12:00:00",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

