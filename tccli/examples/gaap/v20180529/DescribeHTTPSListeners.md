**Example 1: Querying the HTTPS Listener Information**

Query the HTTPS listener information.

Input: 

```
tccli gaap DescribeHTTPSListeners --cli-unfold-argument  \
    --ProxyId link-n9ha8jzl \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 11,
        "ListenerSet": [
            {
                "ForwardProtocol": "HTTPS",
                "ClientCertificateId": null,
                "CertificateId": "Sv8lFuYh",
                "Protocol": "HTTPS",
                "CertificateAlias": "lagameft01_test勿删除",
                "AuthType": 0,
                "ListenerId": "listener-eqq49dct",
                "ListenerStatus": 0,
                "ListenerName": "连通性测试httpstohttps443",
                "ClientCertificateAlias": null,
                "CreateTime": 1563340571,
                "Port": 443
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
                "Port": 1443
            }
        ],
        "RequestId": "db5cebe8-b79a-401c-8704-388776fae938"
    }
}
```

