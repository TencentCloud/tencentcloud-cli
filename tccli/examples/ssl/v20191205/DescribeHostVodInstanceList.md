**Example 1: 云点播实例列表**

云点播实例列表

Input: 

```
tccli ssl DescribeHostVodInstanceList --cli-unfold-argument  \
    --CertificateId abc \
    --IsCache 1 \
    --Filters.0.FilterKey abc \
    --Filters.0.FilterValue abc \
    --ResourceType abc \
    --OldCertificateId abc
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

