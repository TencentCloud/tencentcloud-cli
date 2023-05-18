**Example 1: 查询证书live云资源部署实例列表**

查询证书live云资源部署实例列表

Input: 

```
tccli ssl DescribeHostLiveInstanceList --cli-unfold-argument  \
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
                "Domain": "abc",
                "CertId": "abc",
                "Status": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

