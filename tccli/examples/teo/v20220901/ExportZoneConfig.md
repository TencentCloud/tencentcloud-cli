**Example 1: 导出站点配置**

导出站点 zone-21xfqlh5qjee 下的七层加速配置。

Input: 

```
tccli teo ExportZoneConfig --cli-unfold-argument  \
    --ZoneId zone-21xfqlh5qjee \
    --Types L7AccelerationConfig
```

Output: 
```
{
    "Response": {
        "Content": "{\"FormatVersion\":\"1.0\",\"ZoneConfig\": {\"SmartRouting\": {\"Switch\": \"off\"}, \"Cache\": {\"CustomTime\": {\"Switch\": \"on\", \"CacheTime\": 604800}}, \"MaxAge\": {\"FollowOrigin\": \"on\", \"CacheTime\": 600}, \"CacheKey\": {\"FullURLCache\": \"off\", \"QueryString\": {\"Switch\": \"on\", \"Action\": \"includeCustom\", \"Values\": [\"key1\", \"key2\"]}, \"IgnoreCase\": \"on\"}, \"CachePrefresh\": {\"Switch\": \"off\", \"CacheTimePercent\": 90}, \"OfflineCache\": {\"Switch\": \"on\"}, \"Compression\": {\"Switch\": \"on\", \"Algorithms\": [\"brotli\", \"gzip\"]}, \"ImageOptimize\": {\"Switch\": \"off\"}, \"ForceRedirectHTTPS\": {\"Switch\": \"on\", \"RedirectStatusCode\": 302}, \"HSTS\": {\"Switch\": \"on\", \"IncludeSubDomains\": \"on\", \"Timeout\": 16070400, \"Preload\": \"on\"}, \"TLSConfig\": {\"CipherSuite\": \"loose-v2023\", \"Version\": [\"TLSv1\", \"TLSv1.1\", \"TLSv1.2\", \"TLSv1.3\"]}, \"OCSPStapling\": {\"Switch\": \"off\"}, \"HTTP2\": {\"Switch\": \"on\"}, \"QUIC\": {\"Switch\": \"off\"}, \"UpstreamHTTP2\": {\"Switch\": \"off\"}, \"IPv6\": {\"Switch\": \"off\"}, \"WebSocket\": {\"Switch\": \"on\", \"Timeout\": 30}, \"PostMaxSize\": {\"Switch\": \"on\", \"MaxSize\": 838860800}, \"ClientIPHeader\": {\"Switch\": \"off\", \"HeaderName\": \"\"}, \"ClientIPCountry\": {\"Switch\": \"on\", \"HeaderName\": \"EO-Client-IPCountry\"}, \"gRPC\": {\"Switch\": \"off\"}, \"AccelerateMainland\": {\"Switch\": \"off\"}, \"StandardDebug\": {\"Switch\": \"on\", \"AllowClientIPList\": [\"1.2.3.4\"], \"Expires\": \"2023-11-04T04:46:28Z\"}}, \"Rules\": [{\"RuleName\": \"未命名规则\", \"Branches\": [{\"Condition\": \"${http.request.host} matches '.*'\", \"Actions\": [{\"Name\": \"UpstreamURLRewrite\", \"Parameters\": {\"Type\": \"Path\", \"Action\": \"rmvPrefix\", \"Value\": \"/prefix\"}}], \"SubRules\": [{\"Branches\": [{\"Condition\": \"${http.request.file_extension} in ['.jpg']\", \"Actions\": [{\"Name\": \"PostMaxSize\", \"Parameters\": {\"Switch\": \"on\", \"MaxSize\": 524288000}}]}]}, {\"Branches\": [{\"Condition\": \"${http.request.file_extension} in ['.png']\", \"Actions\": [{\"Name\": \"PostMaxSize\", \"Parameters\": {\"Switch\": \"on\", \"MaxSize\": 209715200}}]}]}]}]}]}",
        "RequestId": "5e0a2b4e-dw6d-4dsa-ac39-1706cbf8a703"
    }
}
```

