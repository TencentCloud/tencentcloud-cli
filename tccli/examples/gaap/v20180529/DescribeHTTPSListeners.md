**Example 1: 查询HTTPS监听器信息**

查询HTTPS监听器信息

Input: 

```
tccli gaap DescribeHTTPSListeners --cli-unfold-argument  \
    --ProxyId link-n9ha8jzl \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ListenerSet": [
            {
                "ListenerId": "abc",
                "ListenerName": "abc",
                "Port": 1,
                "Protocol": "abc",
                "ListenerStatus": 1,
                "CertificateId": "abc",
                "ForwardProtocol": "abc",
                "CreateTime": 1,
                "CertificateAlias": "abc",
                "ClientCertificateId": "abc",
                "AuthType": 0,
                "ClientCertificateAlias": "abc",
                "PolyClientCertificateAliasInfo": [
                    {
                        "CertificateId": "abc",
                        "CertificateAlias": "abc"
                    }
                ],
                "Http3Supported": 0,
                "ProxyId": "abc",
                "GroupId": "abc",
                "TLSSupportVersion": [
                    "abc"
                ],
                "TLSCiphers": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

