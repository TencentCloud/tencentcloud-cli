**Example 1: 更新域名源站配置**

更新域名源站配置

Input: 

```
tccli cdn ModifyDomainConfig --cli-unfold-argument  \
    --Domain www.test.com \
    --Route Origin.Origins \
    --Value {"update":["1.1.1.1"]}
```

Output: 
```
{
    "Response": {
        "RequestId": "eb029ee0-7e91-4a18-86f3-7fac952a446e"
    }
}
```

**Example 2: 更新域名回源超时配置**

更新域名回源超时配置

Input: 

```
tccli cdn ModifyDomainConfig --cli-unfold-argument  \
    --Domain www.test.com \
    --Route OriginPullTimeout \
    --Value {"update":{"ConnectTimeout":10,"ReceiveTimeout":10}}
```

Output: 
```
{
    "Response": {
        "RequestId": "23cd4005-496f-4bc4-87d8-ab348d5b0c21"
    }
}
```

**Example 3: 更新域名回源建连超时时间**

更新域名回源建连超时时间

Input: 

```
tccli cdn ModifyDomainConfig --cli-unfold-argument  \
    --Domain www.test.com \
    --Route OriginPullTimeout.ConnectTimeout \
    --Value {"update":10}
```

Output: 
```
{
    "Response": {
        "RequestId": "23cd4005-496f-4bc4-87d8-ab348d5b0c11"
    }
}
```

**Example 4: 更新 HTTPS 服务器证书 ID（在 SSL 证书管理进行证书托管时自动生成）**

更新 HTTPS 服务器证书 ID（在 SSL 证书管理进行证书托管时自动生成）

Input: 

```
tccli cdn ModifyDomainConfig --cli-unfold-argument  \
    --Domain www.test.com \
    --Route Https.CertInfo.CertId \
    --Value {"update":"0VpOXiPz"}
```

Output: 
```
{
    "Response": {
        "RequestId": "56a166ec-d784-4001-a850-7d62a5c07971"
    }
}
```

