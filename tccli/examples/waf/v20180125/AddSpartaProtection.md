**Example 1: 添加Spart防护域名**



Input: 

```
tccli waf AddSpartaProtection --cli-unfold-argument  \
    --Domain test1.qcloud.com \
    --CertType 0 \
    --IsCdn 0 \
    --IsGray 0 \
    --UpstreamType 0 \
    --IsHttp2 0 \
    --IsWebsocket 0 \
    --LoadBalance 0 \
    --SrcList 1.1.1.1 \
    --Ports.0.Port 80 \
    --Ports.0.Protocol http \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --Ports.0.NginxServerId 0 \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "RequestId": "9ee8be5b-6caa-4c39-ab70-890e0e673515"
    }
}
```

**Example 2: 重复添加的场景**



Input: 

```
tccli waf AddSpartaProtection --cli-unfold-argument  \
    --Domain test.qcloud.com \
    --CertType 0 \
    --IsCdn 0 \
    --IsGray 0 \
    --UpstreamType 0 \
    --IsHttp2 0 \
    --IsWebsocket 0 \
    --LoadBalance 0 \
    --SrcList 1.1.1.1 \
    --Ports.0.Port 80 \
    --Ports.0.Protocol http \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --Ports.0.NginxServerId 0 \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "RequestId": "4f284280-a493-4932-95f4-3d87e7320b3e"
    }
}
```

