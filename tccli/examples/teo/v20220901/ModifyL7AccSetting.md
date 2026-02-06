**Example 1: 修改站点加速全局配置**

修改站点加速全局配置。

Input: 

```
tccli teo ModifyL7AccSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --ZoneConfig.SmartRouting.Switch on \
    --ZoneConfig.Cache.CustomTime.CacheTime 2592000 \
    --ZoneConfig.Cache.CustomTime.Switch off \
    --ZoneConfig.Cache.FollowOrigin.DefaultCache on \
    --ZoneConfig.Cache.FollowOrigin.DefaultCacheStrategy on \
    --ZoneConfig.Cache.FollowOrigin.DefaultCacheTime 0 \
    --ZoneConfig.Cache.FollowOrigin.Switch on \
    --ZoneConfig.Cache.NoCache.Switch off \
    --ZoneConfig.MaxAge.FollowOrigin on \
    --ZoneConfig.MaxAge.CacheTime 600 \
    --ZoneConfig.CacheKey.FullURLCache on \
    --ZoneConfig.CacheKey.IgnoreCase off \
    --ZoneConfig.CacheKey.QueryString.Action includeCustom \
    --ZoneConfig.CacheKey.QueryString.Switch off \
    --ZoneConfig.CachePrefresh.CacheTimePercent 90 \
    --ZoneConfig.CachePrefresh.Switch on \
    --ZoneConfig.OfflineCache.Switch on \
    --ZoneConfig.Compression.Algorithms brotli gzip \
    --ZoneConfig.Compression.Switch on \
    --ZoneConfig.ForceRedirectHTTPS.RedirectStatusCode 302 \
    --ZoneConfig.ForceRedirectHTTPS.Switch off \
    --ZoneConfig.HSTS.IncludeSubDomains off \
    --ZoneConfig.HSTS.Timeout 0 \
    --ZoneConfig.HSTS.Preload off \
    --ZoneConfig.HSTS.Switch off \
    --ZoneConfig.TLSConfig.Version TLSv1 TLSv1.1 TLSv1.2 TLSv1.3 \
    --ZoneConfig.TLSConfig.CipherSuite loose-v2023 \
    --ZoneConfig.OCSPStapling.Switch off \
    --ZoneConfig.HTTP2.Switch off \
    --ZoneConfig.QUIC.Switch off \
    --ZoneConfig.UpstreamHTTP2.Switch off \
    --ZoneConfig.IPv6.Switch off \
    --ZoneConfig.WebSocket.Switch off \
    --ZoneConfig.WebSocket.Timeout 30 \
    --ZoneConfig.PostMaxSize.MaxSize 524288000 \
    --ZoneConfig.PostMaxSize.Switch on \
    --ZoneConfig.ClientIPHeader.HeaderName  \
    --ZoneConfig.ClientIPHeader.Switch off \
    --ZoneConfig.ClientIPCountry.HeaderName  \
    --ZoneConfig.ClientIPCountry.Switch off \
    --ZoneConfig.Grpc.Switch off \
    --ZoneConfig.NetworkErrorLogging.Switch on \
    --ZoneConfig.AccelerateMainland.Switch off \
    --ZoneConfig.StandardDebug.Expires 1969-12-31T16:00:00Z \
    --ZoneConfig.StandardDebug.Switch off
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 2: 修改站点加速全局 IPv6 访问配置**

针对站点下所有域名开启 IPv6 访问

Input: 

```
tccli teo ModifyL7AccSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --ZoneConfig.IPv6.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 3: 修改站点加速全局 QUIC 配置**

针对站点下所有域名开启 QUIC

Input: 

```
tccli teo ModifyL7AccSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --ZoneConfig.QUIC.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 4: 修改站点加速全局节点缓存 TTL 配置**

针对站点下所有域名将缓存配置为不缓存

Input: 

```
tccli teo ModifyL7AccSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --ZoneConfig.Cache.NoCache.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

