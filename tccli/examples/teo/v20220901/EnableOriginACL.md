**Example 1: 开启指定4/7层实例回源白名单**

开启7层实例"www.qq.com"和4层实例"proxy-19389e5dwwxfs"的回源白名单。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L7EnableMode specific \
    --L7Hosts www.qq.com \
    --L4EnableMode specific \
    --L4ProxyIds proxy-19389e5dwwxfs
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706cbf8a869"
    }
}
```

**Example 2: 开启指定4层实例的回源白名单**

4层实例"proxy-19389e5dwwxfs"的回源白名单。

Input: 

```
tccli teo EnableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --L4EnableMode specific \
    --L4ProxyIds proxy-19389e5dwwxfs
```

Output: 
```
{
    "Response": {
        "RequestId": "9e0a2b4f-df6d-4d2a-ac39-1706cbf8a869"
    }
}
```

**Example 3: 开启指定7层实例的回源白名单**

开启7层实例"www.qq.com"的回源白名单。

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

**Example 4: 开启站点下所有7层实例的回源白名单**

开启站点下所有7层实例的回源白名单。

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

**Example 5: 开启站点下所有4层实例的回源白名单**

开启站点下所有4层实例的回源白名单。

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

**Example 6: 为站点下的所有实例开启回源白名单**

开启站点"zone-276zs184g93m"下的所有实例的回源白名单。

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

