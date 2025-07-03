**Example 1: 站点首次启用源站防护，并配置为指定七层加速域名/四层代理实例启用特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点开启源站防护，并配置七层加速域名‘www.qq.com’和四层代理实例‘sid-19389e5dwwxfs’启用特定回源 IP 网段回源。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L7EnableMode specific \
    --L7Hosts www.qq.com \
    --L4EnableMode specific \
    --L4ProxyIds sid-19389e5dwwxfs
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706cbf8a869"
    }
}
```

**Example 2: 站点首次启用源站防护，并配置为指定七层加速域名启用特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点开启源站防护，并配置七层加速域名‘www.qq.com’启用特定回源 IP 网段回源。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L7EnableMode specific \
    --L7Hosts www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706cbf8a869"
    }
}
```

**Example 3: 站点首次启用源站防护，并配置为指定四层代理实例启用特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点开启源站防护，并配置四层代理实例‘sid-19389e5dwwxfs’启用特定回源 IP 网段回源。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L4EnableMode specific \
    --L4ProxyIds sid-19389e5dwwxfs
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706cbf8a869"
    }
}
```

**Example 4: 站点首次启用源站防护，并配置站点下所有七层加速域名和四层代理实例启用特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点开启源站防护，并配置所有的七层加速域名和四层代理实例启用特定回源 IP 网段回源。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L7EnableMode all \
    --L4EnableMode all
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706wdf8a869"
    }
}
```

**Example 5: 站点首次启用源站防护，并配置站点下所有七层加速域名启用特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点开启源站防护，并配置所有的七层加速域名启用特定回源 IP 网段回源。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L7EnableMode all
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706wdf8a869"
    }
}
```

**Example 6: 站点首次启用源站防护，并配置站点下所有四层代理实例启用特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点开启源站防护，并配置所有的四层代理实例启用特定回源 IP 网段回源。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L4EnableMode all
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706wdf8a869"
    }
}
```

