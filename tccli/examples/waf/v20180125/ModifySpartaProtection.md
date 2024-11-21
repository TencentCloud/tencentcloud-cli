**Example 1: 修改SaaS型WAF域名**

修改SaaS型WAF域名

Input: 

```
tccli waf ModifySpartaProtection --cli-unfold-argument  \
    --Ports.0.NginxServerId 230056 \
    --Ports.0.Port 80 \
    --Ports.0.Protocol http \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --Ports.1.NginxServerId 321607 \
    --Ports.1.Port 443 \
    --Ports.1.Protocol https \
    --Ports.1.UpstreamPort 80 \
    --Ports.1.UpstreamProtocol http \
    --Domain randygz8.qcloudwaf.com \
    --DomainId 7d58ebf3db7e5f7e8f91eb017c6a7b31 \
    --SrcList 114.132.246.237 114.132.246.239 \
    --Weights 10 10 \
    --UpstreamType 0 \
    --HttpsRewrite 0 \
    --CertType 2 \
    --ActiveCheck 0 \
    --SSLId H0LMTjmj \
    --IsCdn 1 \
    --UpstreamScheme http \
    --HttpsUpstreamPort 80 \
    --IsGray 0 \
    --IsHttp2 0 \
    --IsWebsocket 0 \
    --ProxyBuffer 1 \
    --IsKeepAlive 1 \
    --LoadBalance 0 \
    --InstanceID waf_2kw60zgy0508e8j3 \
    --Anycast 0 \
    --CipherTemplate 2 \
    --TLSVersion 3 \
    --Ciphers 0 1 12 13 22 \
    --ProxyReadTimeout 10 \
    --ProxySendTimeout 300 \
    --SniHost randy.sni.com \
    --SniType 1 \
    --IpHeaders x-real-ip \
    --XFFReset 0 \
    --UpstreamHost randy.upstream.com \
    --Note randy domain \
    --ProbeStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "13b8a309-3e7d-4393-91a4-271bf6d5dd71"
    }
}
```

