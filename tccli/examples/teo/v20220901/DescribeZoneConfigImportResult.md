**Example 1: 查询配置导入结果**

查询站点 zone-21xfqlh4qjee 下七层加速配置项的导入结果。

Input: 

```
tccli teo DescribeZoneConfigImportResult --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --TaskId 33mz68e4gwka
```

Output: 
```
{
    "Response": {
        "RequestId": "88215c08-67de-4c7d-974e-a14461816f5b",
        "Status": "success",
        "Message": "success",
        "Content": "{\"FormatVersion\":\"1.0\",\"ZoneConfig\": {\"SmartRouting\": {\"Switch\": \"off\"}, \"Cache\": {\"CustomTime\": {\"Switch\": \"on\", \"CacheTime\": 604800}}, \"MaxAge\": {\"FollowOrigin\": \"on\", \"CacheTime\": 600}, \"CacheKey\": {\"FullURLCache\": \"off\", \"QueryString\": {\"Switch\": \"on\", \"Action\": \"includeCustom\", \"Values\": [\"key1\", \"key2\"]}, \"IgnoreCase\": \"on\"}, \"CachePrefresh\": {\"Switch\": \"off\", \"CacheTimePercent\": 90}, \"OfflineCache\": {\"Switch\": \"on\"}, \"Compression\": {\"Switch\": \"on\", \"Algorithms\": [\"brotli\", \"gzip\"]}, \"ImageOptimize\": {\"Switch\": \"off\"}, \"ForceRedirectHTTPS\": {\"Switch\": \"on\", \"RedirectStatusCode\": 302}, \"HSTS\": {\"Switch\": \"on\", \"IncludeSubDomains\": \"on\", \"Timeout\": 16070400, \"Preload\": \"on\"}, \"TLSConfig\": {\"CipherSuite\": \"loose-v2023\", \"Version\": [\"TLSv1\", \"TLSv1.1\", \"TLSv1.2\", \"TLSv1.3\"]}, \"OCSPStapling\": {\"Switch\": \"off\"}, \"HTTP2\": {\"Switch\": \"on\"}, \"QUIC\": {\"Switch\": \"off\"}, \"UpstreamHTTP2\": {\"Switch\": \"off\"}, \"IPv6\": {\"Switch\": \"off\"}, \"WebSocket\": {\"Switch\": \"on\", \"Timeout\": 30}, \"PostMaxSize\": {\"Switch\": \"on\", \"MaxSize\": 838860800}, \"ClientIPHeader\": {\"Switch\": \"off\", \"HeaderName\": \"\"}, \"ClientIPCountry\": {\"Switch\": \"on\", \"HeaderName\": \"EO-Client-IPCountry\"}, \"gRPC\": {\"Switch\": \"off\"}, \"AccelerateMainland\": {\"Switch\": \"off\"}, \"StandardDebug\": {\"Switch\": \"on\", \"AllowClientIPList\": [\"1.2.3.4\"], \"Expires\": \"2023-11-04T04:46:28Z\"}}, \"Rules\": [{\"RuleName\": \"未命名规则\", \"Branches\": [{\"Condition\": \"${http.request.host} matches \".*\"\", \"Actions\": [{\"Name\": \"UpstreamURLRewrite\", \"Parameters\": {\"Type\": \"Path\", \"Action\": \"rmvPrefix\", \"Value\": \"/prefix\"}}], \"SubRules\": [{\"Branches\": [{\"Condition\": \"${http.request.file_extension} in [\".jpg\"]\", \"Actions\": [{\"Name\": \"PostMaxSize\", \"Parameters\": {\"Switch\": \"on\", \"MaxSize\": 524288000}}]}]}, {\"Branches\": [{\"Condition\": \"${http.request.file_extension} in [\".png\"]\", \"Actions\": [{\"Name\": \"PostMaxSize\", \"Parameters\": {\"Switch\": \"on\", \"MaxSize\": 209715200}}]}]}]}]}]}",
        "ImportTime": "2024-10-13T23:58:00+08:00",
        "FinishTime": "2024-10-13T23:59:00+08:00"
    }
}
```

