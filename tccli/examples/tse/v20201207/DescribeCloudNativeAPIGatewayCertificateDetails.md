**Example 1: 查询云原生网关单个证书详情**

查询云原生网关单个证书详情

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayCertificateDetails --cli-unfold-argument  \
    --GatewayId abc \
    --Id abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "Cert": {
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
        },
        "RequestId": "abc"
    }
}
```

