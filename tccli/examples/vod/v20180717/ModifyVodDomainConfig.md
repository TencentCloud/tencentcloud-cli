**Example 1: 设置域名的 QUIC 配置**

设置域名的 QUIC 配置

Input: 

```
tccli vod ModifyVodDomainConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --QUICConfig.Status Enabled
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e1"
    }
}
```

**Example 2: 设置域名的 Key 防盗链**

设置域名的 Key 防盗链

Input: 

```
tccli vod ModifyVodDomainConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --UrlSignatureAuthPolicy.Status Enabled \
    --UrlSignatureAuthPolicy.EncryptedKey AKIDwgcP1i
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e1"
    }
}
```

**Example 3: 设置域名的 Referer 防盗链**

设置域名的 Referer 防盗链

Input: 

```
tccli vod ModifyVodDomainConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --RefererAuthPolicy.Status Enabled \
    --RefererAuthPolicy.AuthType Black \
    --RefererAuthPolicy.Referers example.com \
    --RefererAuthPolicy.BlankRefererAllowed Yes
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e1"
    }
}
```

**Example 4: 设置域名的 IP 黑名单**

设置域名的 IP 黑名单，拦截来自该黑名单的请求对加速域名的访问。

Input: 

```
tccli vod ModifyVodDomainConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --IPFilterPolicy.Status Enabled \
    --IPFilterPolicy.FilterType Black \
    --IPFilterPolicy.IPList 1.1.1.1 2.3.4.5
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-55941457e1"
    }
}
```

**Example 5: 设置域名的 IP 白名单**

设置域名的 IP 白名单，允许来自该白名单的请求对加速域名的访问。

Input: 

```
tccli vod ModifyVodDomainConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --IPFilterPolicy.Status Enabled \
    --IPFilterPolicy.FilterType White \
    --IPFilterPolicy.IPList 1.2.3.4 2.3.4.5
```

Output: 
```
{
    "Response": {
        "RequestId": "1536ae8d8e-dce3-4551-9d4b-55f78201"
    }
}
```

