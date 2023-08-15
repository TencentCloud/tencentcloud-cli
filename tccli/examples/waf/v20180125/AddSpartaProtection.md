**Example 1: 重复添加的场景**

重复添加的场景

Input: 

```
tccli waf AddSpartaProtection --cli-unfold-argument  \
    --Domain test.qcloud.com \
    --LoadBalance 0 \
    --Edition clb-waf \
    --UpstreamType 0 \
    --CertType 0 \
    --Ports.0.NginxServerId 0 \
    --Ports.0.Protocol http \
    --Ports.0.Port 80 \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --SrcList 1.1.1.1 \
    --IsCdn 0 \
    --IsWebsocket 0 \
    --IsGray 0 \
    --IsHttp2 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "域名已经存在，请勿重复添加"
        },
        "RequestId": "4f284280-a493-4932-95f4-3d87e7320b3e"
    }
}
```

**Example 2: 添加域名**

添加域名

Input: 

```
tccli waf AddSpartaProtection --cli-unfold-argument  \
    --UpstreamScheme http \
    --IsGray 1 \
    --Domain lucas0621.qcloudwaf.com \
    --LoadBalance 1 \
    --HttpsUpstreamPort 80 \
    --InstanceID lucas \
    --UpstreamType 1 \
    --UpstreamDomain lucas0622.qcloudwaf.com \
    --IsWebsocket 1 \
    --IsHttp2 1 \
    --Edition sass \
    --CertType 0 \
    --Weights 1 \
    --IsKeepAlive 1 \
    --ActiveCheck 1 \
    --IsCdn 1 \
    --TLSVersion 1 \
    --Anycast 1 \
    --Ports.0.NginxServerId 0 \
    --Ports.0.Protocol http \
    --Ports.0.Port 80 \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --HttpsRewrite 1
```

Output: 
```
{
    "Response": {
        "RequestId": "87c8499e-3748-4bb0-9740-b2683a003975"
    }
}
```

**Example 3: 添加域名-1**

添加域名-1

Input: 

```
tccli waf AddSpartaProtection --cli-unfold-argument  \
    --UpstreamScheme http \
    --IsGray 1 \
    --Domain lucas0919.qcloudwaf.com \
    --LoadBalance 1 \
    --HttpsUpstreamPort 80 \
    --InstanceID lucas \
    --UpstreamType 1 \
    --UpstreamDomain lucas0622.qcloudwaf.com \
    --IsWebsocket 1 \
    --IsHttp2 1 \
    --Edition saas \
    --CertType 0 \
    --Weights 1 \
    --IsKeepAlive 1 \
    --ActiveCheck 1 \
    --IsCdn 1 \
    --TLSVersion 3 \
    --Ports.0.NginxServerId 0 \
    --Ports.0.Protocol http \
    --Ports.0.Port 80 \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --HttpsRewrite 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a5e5757a-2b04-4d56-a049-54eb8f053e75"
    }
}
```

**Example 4: 添加SAAS-WAF防护域名**

添加SAAS-WAF防护域名

Input: 

```
tccli waf AddSpartaProtection --cli-unfold-argument  \
    --Domain test1.qcloud.com \
    --LoadBalance 0 \
    --Edition clb-waf \
    --UpstreamType 0 \
    --CertType 0 \
    --Ports.0.NginxServerId 0 \
    --Ports.0.Protocol http \
    --Ports.0.Port 80 \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --SrcList 1.1.1.1 \
    --IsCdn 0 \
    --IsWebsocket 0 \
    --IsGray 0 \
    --IsHttp2 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9ee8be5b-6caa-4c39-ab70-890e0e673515"
    }
}
```

