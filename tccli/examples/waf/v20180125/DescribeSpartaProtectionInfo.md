**Example 1: waf斯巴达-获取防护域名信息**



Input: 

```
tccli waf DescribeSpartaProtectionInfo --cli-unfold-argument  \
    --Domain www.test1.com \
    --Edition sprata-waf
```

Output: 
```
{
    "Response": {
        "Cert": "test",
        "CertType": "1",
        "Cname": "",
        "Domain": "www.test1.com",
        "DomainId": "",
        "Engine": "1",
        "GrayAreas": [
            "n"
        ],
        "HttpsRewrite": "0",
        "HttpsUpstreamPort": "0",
        "IsCdn": "0",
        "IsGray": "0",
        "IsHttp2": "0",
        "IsWebsocket": "0",
        "LoadBalance": "0",
        "Mode": "1",
        "Ports": [],
        "PrivateKey": "xxxx",
        "RequestId": "1548ac10-3e48-4cee-b71b-fc1071421761",
        "SrcList": [
            "1.1.1."
        ],
        "Sslid": "",
        "Status": "2",
        "UpstreamDomain": "",
        "UpstreamScheme": "http",
        "UpstreamType": "0",
        "Level": "200",
        "IsKeepAlive": "1",
        "Anycast": "1"
    }
}
```

