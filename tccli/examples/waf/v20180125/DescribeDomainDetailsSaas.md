**Example 1: 查询单个saaswaf域名详情**

查询单个saaswaf域名详情

Input: 

```
tccli waf DescribeDomainDetailsSaas --cli-unfold-argument  \
    --Domain jackysaas010.qcloudwaf.com \
    --DomainId eca17401f4e55f4b946aa37a2212b729 \
    --InstanceId waf_2kzew5sy0qzrn81b
```

Output: 
```
{
    "Response": {
        "RequestId": "4552f857-a877-4ab1-b2f3-9d31930b7f4a",
        "DomainsPartInfo": {
            "Domain": "jackysaas010.qcloudwaf.com",
            "DomainId": "eca17401f4e55f4b946aa37a2212b729",
            "InstanceId": "waf_2kzew5sy0qzrn81b",
            "Edition": "sparta-waf",
            "InstanceName": "test010",
            "Cert": "-----BEGIN CERTIFICATE----- customer cert -----END CERTIFICATE-----",
            "CertType": 0,
            "Cls": 1,
            "CreateTime": "2024-06-05 11:23:08",
            "Cname": "dc1f8442749285feb56b39ac57049213.qcloudcjgj.com",
            "Engine": 1,
            "HttpsRewrite": 0,
            "HttpsUpstreamPort": "80",
            "IsKeepAlive": 1,
            "IsCdn": 0,
            "IsGray": 0,
            "IsHttp2": 0,
            "IsWebsocket": 0,
            "LoadBalance": 0,
            "Mode": 1,
            "PrivateKey": "-----BEGIN RSA PRIVATE KEY----- customer key -----END RSA PRIVATE KEY-----",
            "SSLId": "cnKsi3a",
            "UpstreamDomain": "jack.upstream.com",
            "UpstreamScheme": "http",
            "UpstreamType": 0,
            "SrcList": [
                "143.26.159.6",
                "143.26.159.8"
            ],
            "Weights": [
                "10",
                "10"
            ],
            "Ports": [
                {
                    "NginxServerId": 235574,
                    "Port": "80",
                    "Protocol": "http",
                    "UpstreamPort": "80",
                    "UpstreamProtocol": "http"
                }
            ],
            "ActiveCheck": 0,
            "TLSVersion": 3,
            "Ciphers": [],
            "CipherTemplate": 1,
            "ProxyReadTimeout": 300,
            "ProxySendTimeout": 300,
            "SniType": 2,
            "SniHost": "jack.sni.com",
            "IpHeaders": [
                "x-real-ip"
            ],
            "XFFReset": 0,
            "Note": "jack domain",
            "Level": "300",
            "UpstreamHost": "jack.upstream.com",
            "ProxyBuffer": 1,
            "GmType": 0,
            "GmCertType": 0,
            "Labels": [
                "jack label"
            ]
        }
    }
}
```

