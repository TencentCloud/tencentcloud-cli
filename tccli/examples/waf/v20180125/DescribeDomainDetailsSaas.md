**Example 1: 查询单个saaswaf域名详情**

查询单个saaswaf域名详情

Input: 

```
tccli waf DescribeDomainDetailsSaas --cli-unfold-argument  \
    --Domain lucasssli3.qcloud.com \
    --DomainId 20200728142847163546341 \
    --InstanceId waf_000000002
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "DomainsPartInfo": {
            "Domain": "",
            "DomainId": "",
            "InstanceId": "",
            "Edition": "",
            "InstanceName": "",
            "Cert": "",
            "CertType": 0,
            "Cls": 0,
            "CreateTime": "",
            "Cname": "",
            "Engine": 0,
            "SniType": 0,
            "SniHost": "",
            "ProxySendTimeout": 0,
            "ProxyReadTimeout": 0,
            "Ciphers": [
                0
            ],
            "HttpsRewrite": 0,
            "HttpsUpstreamPort": "",
            "IsKeepAlive": 0,
            "IsCdn": 0,
            "IsGray": 0,
            "IsHttp2": 0,
            "IsWebsocket": 0,
            "LoadBalance": 0,
            "Mode": 0,
            "PrivateKey": "",
            "SSLId": "",
            "UpstreamDomain": "",
            "UpstreamScheme": "",
            "UpstreamType": 0,
            "TLSVersion": 0,
            "CipherTemplate": 0,
            "SrcList": [],
            "Ports": [],
            "ActiveCheck": 1,
            "Weights": [
                "10,10,10"
            ],
            "IpHeaders": [
                "abc"
            ],
            "XFFReset": 0
        }
    }
}
```

