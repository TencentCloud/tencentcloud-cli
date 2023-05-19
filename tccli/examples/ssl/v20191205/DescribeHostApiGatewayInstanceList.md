**Example 1: 查询证书ddos云资源部署实例列表**

查询证书ddos云资源部署实例列表

Input: 

```
tccli ssl DescribeHostApiGatewayInstanceList --cli-unfold-argument  \
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
                "ServiceId": "abc",
                "ServiceName": "abc",
                "Domain": "abc",
                "CertId": "abc",
                "Protocol": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

