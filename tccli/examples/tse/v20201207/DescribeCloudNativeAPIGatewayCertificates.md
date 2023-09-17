**Example 1: 查询云原生网关证书列表**

查询云原生网关证书列表

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayCertificates --cli-unfold-argument  \
    --GatewayId abc \
    --Limit 0 \
    --Offset 0 \
    --Filters.0.Key abc \
    --Filters.0.Value abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "Total": 0,
            "CertificatesList": [
                {
                    "Name": "abc",
                    "Id": "abc",
                    "BindDomains": [
                        "abc"
                    ],
                    "Status": "abc",
                    "Crt": "abc",
                    "Key": "abc",
                    "ExpireTime": "abc",
                    "CreateTime": "abc",
                    "IssueTime": "abc",
                    "CertSource": "abc",
                    "CertId": "abc"
                }
            ],
            "Pages": 0
        },
        "RequestId": "abc"
    }
}
```

