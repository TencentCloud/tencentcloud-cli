**Example 1: 添加SaaS型WAF防护域名**

添加SaaS型WAF防护域名

Input: 

```
tccli waf AddSpartaProtection --cli-unfold-argument  \
    --Ports.0.NginxServerId 0 \
    --Ports.0.Port 80 \
    --Ports.0.Protocol http \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --Domain randy.qcloudwaf.com \
    --SrcList 125.36.35.4 \
    --UpstreamType 0 \
    --HttpsRewrite 0 \
    --CertType 0 \
    --IsCdn 3 \
    --IsGray 0 \
    --IsHttp2 0 \
    --IsWebsocket 0 \
    --ProxyBuffer 1 \
    --ActiveCheck 0 \
    --CipherTemplate 1 \
    --TLSVersion 3 \
    --IsKeepAlive 1 \
    --LoadBalance 0 \
    --InstanceID waf_2kw60zgy0908e8j3 \
    --Anycast 0 \
    --ProxyReadTimeout 300 \
    --ProxySendTimeout 300 \
    --SniHost randy.sni.com \
    --SniType 0 \
    --IpHeaders x-real-ip \
    --XFFReset 0 \
    --UpstreamHost randy.upstream.com \
    --Note randy test domain \
    --ProbeStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9ee8be5b-6caa-4c39-ab70-890e0e673515"
    }
}
```

