**Example 1: 云点播实例列表**

云点播实例列表

Input: 

```
tccli ssl DescribeHostVodInstanceList --cli-unfold-argument  \
    --CertificateId yX1eNoWz \
    --IsCache 1 \
    --Filters.0.FilterKey DomainMatch \
    --Filters.0.FilterValue 1 \
    --OldCertificateId HJ*****gg
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "hatm.cn",
                "CertId": "yX1eNoWz"
            },
            {
                "Domain": "www.hama.cn",
                "CertId": "yX2eNoWz"
            }
        ],
        "TotalCount": 2,
        "RequestId": "ba893ea5-7862-424e-8daf-000e55931501"
    }
}
```

