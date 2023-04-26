**Example 1: 修改站点Ipv6访问配置**

修改站点Ipv6访问配置。

Input: 

```
tccli teo ModifyZoneSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --Ipv6.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 2: 修改站点Quic访问配置**

修改站点Quic访问配置。

Input: 

```
tccli teo ModifyZoneSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --Quic.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 3: 修改站点缓存过期时间配置**

修改站点缓存过期时间配置。

Input: 

```
tccli teo ModifyZoneSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --CacheConfig.NoCache.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

