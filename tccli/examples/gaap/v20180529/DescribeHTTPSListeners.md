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
                "ListenerId": "listener-12345",
                "ListenerName": "listener-name",
                "Port": 1,
                "Protocol": "TCP",
                "ListenerStatus": 1,
                "CertificateId": "cert-12345",
                "ForwardProtocol": "TCP",
                "CreateTime": 1,
                "CertificateAlias": "alias-name",
                "ClientCertificateId": "cert-54321",
                "AuthType": 0,
                "ClientCertificateAlias": "alias-name",
                "PolyClientCertificateAliasInfo": [
                    {
                        "CertificateId": "cert-12345",
                        "CertificateAlias": "cert-alias"
                    }
                ],
                "Http3Supported": 0,
                "ProxyId": "link-12345",
                "GroupId": "lg-12345",
                "TLSSupportVersion": [
                    "TLSv1.1"
                ],
                "TLSCiphers": "GAAP_TLS_CIPHERS_WIDE"
            }
        ],
        "RequestId": "209e95b9-488d-4a58-bc86-810859577af3"
    }
}
```

