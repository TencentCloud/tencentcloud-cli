**Example 1: 证书部署COS实例列表**

证书部署COS实例列表

Input: 

```
tccli ssl DescribeHostCosInstanceList --cli-unfold-argument  \
    --CertificateId abc \
    --IsCache 1 \
    --Filters.0.FilterKey abc \
    --Filters.0.FilterValue abc \
    --ResourceType abc
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "abc",
                "CertId": "abc",
                "Status": "abc",
                "Bucket": "abc",
                "Region": "abc"
            }
        ],
        "TotalCount": 0,
        "AsyncTotalNum": 0,
        "AsyncOffset": 0,
        "AsyncCacheTime": "abc",
        "RequestId": "abc"
    }
}
```

