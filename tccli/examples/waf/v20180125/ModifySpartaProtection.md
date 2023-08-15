**Example 1: 修改域名配置**

修改SAASWAF域名

Input: 

```
tccli waf ModifySpartaProtection --cli-unfold-argument  \
    --Domain www.test.com \
    --LoadBalance 0 \
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

**Example 2: 修改域名接入配置**

修改SAASWAF域名

Input: 

```
tccli waf ModifySpartaProtection --cli-unfold-argument  \
    --Domain lucas0407-1.qcloudwaf.com \
    --LoadBalance 0 \
    --InstanceID waf_2kuj60v200b09bsr \
    --UpstreamType 0 \
    --IsWebsocket 0 \
    --IsHttp2 0 \
    --SrcList 11.148.84.137 \
    --CertType 0 \
    --DomainId eb454223185451fe8b255a82b9d4bf94 \
    --Weights 100 \
    --IsKeepAlive 1 \
    --IsCdn 1 \
    --IsGray 0 \
    --Anycast 0 \
    --Ports.0.NginxServerId 62094 \
    --Ports.0.Protocol http \
    --Ports.0.Port 80 \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --ActiveCheck 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9c553d61-526a-44cf-a874-b24956033973"
    }
}
```

**Example 3: ts**

修改SAASWAF域名

Input: 

```
tccli waf ModifySpartaProtection --cli-unfold-argument  \
    --IsGray 0 \
    --Domain lucas0407-1.qcloudwaf.com \
    --LoadBalance 0 \
    --CipherTemplate 0 \
    --InstanceID waf_2kuj60v200b09bsr \
    --UpstreamType 0 \
    --IsWebsocket 0 \
    --IsHttp2 0 \
    --SrcList 114.132.223.23 \
    --CertType 0 \
    --DomainId eb454223185451fe8b255a82b9d4bf94 \
    --Weights 100 \
    --IsKeepAlive 1 \
    --IsCdn 1 \
    --TLSVersion 3 \
    --Anycast 0 \
    --Ports.0.NginxServerId 62094 \
    --Ports.0.Protocol http \
    --Ports.0.Port 80 \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --ActiveCheck 1
```

Output: 
```
{
    "Response": {
        "RequestId": "13b8a309-3e7d-4393-91a4-271bf6d5dd71"
    }
}
```

**Example 4: Modify-Host-1**

修改SAASWAF域名

Input: 

```
tccli waf ModifySpartaProtection --cli-unfold-argument  \
    --IsGray 0 \
    --Domain lucas0919.qcloudwaf.com \
    --LoadBalance 0 \
    --CipherTemplate 0 \
    --InstanceID lucas \
    --UpstreamType 0 \
    --IsWebsocket 0 \
    --IsHttp2 0 \
    --SrcList 114.132.223.23 \
    --CertType 0 \
    --DomainId e801733b69605960a17388999868512a \
    --Weights 100 \
    --IsKeepAlive 1 \
    --IsCdn 1 \
    --TLSVersion 3 \
    --Anycast 0 \
    --Ports.0.NginxServerId 63953 \
    --Ports.0.Protocol http \
    --Ports.0.Port 80 \
    --Ports.0.UpstreamPort 80 \
    --Ports.0.UpstreamProtocol http \
    --ActiveCheck 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d6bd6f14-926e-4a3e-9a34-bb1dd7d9a51d"
    }
}
```

