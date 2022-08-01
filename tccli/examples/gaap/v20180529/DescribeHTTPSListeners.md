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
        "TotalCount": 11,
        "ListenerSet": [
            {
                "ForwardProtocol": "HTTPS",
                "ClientCertificateId": "123",
                "CertificateId": "Sv8lFuYh",
                "Protocol": "HTTPS",
                "CertificateAlias": "lagameft01_test勿删除",
                "AuthType": 0,
                "ListenerId": "listener-eqq49dct",
                "ListenerStatus": 0,
                "ListenerName": "连通性测试httpstohttps443",
                "ClientCertificateAlias": "sdvadf",
                "CreateTime": 1563340571,
                "Port": 443,
                "PolyClientCertificateAliasInfo": [
                    {
                        "CertificateId": "123",
                        "CertificateAlias": "alis"
                    }
                ]
            },
            {
                "ForwardProtocol": "HTTPS",
                "ClientCertificateId": "",
                "CertificateId": "cert-r79xf99t",
                "Protocol": "HTTPS",
                "CertificateAlias": "boris服务器证书user001",
                "AuthType": 0,
                "ListenerId": "listener-85646933",
                "ListenerStatus": 0,
                "ListenerName": "testcert001",
                "ClientCertificateAlias": null,
                "CreateTime": 1564201158,
                "Port": 1443,
                "PolyClientCertificateAliasInfo": [
                    {
                        "CertificateId": "123",
                        "CertificateAlias": "alis"
                    }
                ]
            }
        ],
        "RequestId": "db5cebe8-b79a-401c-8704-388776fae938"
    }
}
```

