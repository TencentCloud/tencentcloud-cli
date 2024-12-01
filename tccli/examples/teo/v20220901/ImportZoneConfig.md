**Example 1: 导入站点七层加速配置**

导入站点 zone-m2kplohsdc4b 下的七层加速配置。

Input: 

```
tccli teo ImportZoneConfig --cli-unfold-argument  \
    --ZoneId zone-m2kplohsdc4b \
    --Content {"FormatVersion":"1.0","ZoneConfig": {"SmartRouting": {"Switch": "off"}, "Cache": {"CustomTime": {"Switch": "on", "CacheTime": 604800}}, "MaxAge": {"FollowOrigin": "on", "CacheTime": 600}, "CacheKey": {"FullURLCache": "off", "QueryString": {"Switch": "on", "Action": "includeCustom", "Values": ["key1", "key2"]}, "IgnoreCase": "on"}, "CachePrefresh": {"Switch": "off", "CacheTimePercent": 90}, "OfflineCache": {"Switch": "on"}, "Compression": {"Switch": "on", "Algorithms": ["brotli", "gzip"]}, "ImageOptimize": {"Switch": "off"}, "ForceRedirectHTTPS": {"Switch": "on", "RedirectStatusCode": 302}, "HSTS": {"Switch": "on", "IncludeSubDomains": "on", "Timeout": 16070400, "Preload": "on"}, "TLSConfig": {"CipherSuite": "loose-v2023", "Version": ["TLSv1", "TLSv1.1", "TLSv1.2", "TLSv1.3"]}, "OCSPStapling": {"Switch": "off"}, "HTTP2": {"Switch": "on"}, "QUIC": {"Switch": "off"}, "UpstreamHTTP2": {"Switch": "off"}, "IPv6": {"Switch": "off"}, "WebSocket": {"Switch": "on", "Timeout": 30}, "PostMaxSize": {"Switch": "on", "MaxSize": 838860800}, "ClientIPHeader": {"Switch": "off", "HeaderName": ""}, "ClientIPCountry": {"Switch": "on", "HeaderName": "EO-Client-IPCountry"}, "gRPC": {"Switch": "off"}, "AccelerateMainland": {"Switch": "off"}, "StandardDebug": {"Switch": "on", "AllowClientIPList": ["1.2.3.4"], "Expires": "2023-11-04T04:46:28Z"}}, "Rules": [{"RuleName": "未命名规则", "Branches": [{"Condition": "${http.request.host} matches ".*"", "Actions": [{"Name": "UpstreamURLRewrite", "Parameters": {"Type": "Path", "Action": "rmvPrefix", "Value": "/prefix"}}], "SubRules": [{"Branches": [{"Condition": "${http.request.file_extension} in [".jpg"]", "Actions": [{"Name": "PostMaxSize", "Parameters": {"Switch": "on", "MaxSize": 524288000}}]}]}, {"Branches": [{"Condition": "${http.request.file_extension} in [".png"]", "Actions": [{"Name": "PostMaxSize", "Parameters": {"Switch": "on", "MaxSize": 209715200}}]}]}]}]}]}
```

Output: 
```
{
    "Response": {
        "TaskId": "33mz68e4gwka",
        "RequestId": "5e0a2b4e-dw6d-4dsa-ac39-1706cbf8a703"
    }
}
```

**Example 2: 导入站点七层加速配置的站点加速配置**

单独导入站点 zone-m2kplohsdc4b 下七层加速配置的全局加速配置。

Input: 

```
tccli teo ImportZoneConfig --cli-unfold-argument  \
    --ZoneId zone-m2kplohsdc4b \
    --Content {"FormatVersion":"1.0","ZoneConfig": {"SmartRouting": {"Switch": "off"}, "Cache": {"CustomTime": {"Switch": "on", "CacheTime": 604800}}, "MaxAge": {"FollowOrigin": "on", "CacheTime": 600}, "CacheKey": {"FullURLCache": "off", "QueryString": {"Switch": "on", "Action": "includeCustom", "Values": ["key1", "key2"]}, "IgnoreCase": "on"}, "CachePrefresh": {"Switch": "off", "CacheTimePercent": 90}, "OfflineCache": {"Switch": "on"}, "Compression": {"Switch": "on", "Algorithms": ["brotli", "gzip"]}, "ImageOptimize": {"Switch": "off"}, "ForceRedirectHTTPS": {"Switch": "on", "RedirectStatusCode": 302}, "HSTS": {"Switch": "on", "IncludeSubDomains": "on", "Timeout": 16070400, "Preload": "on"}, "TLSConfig": {"CipherSuite": "loose-v2023", "Version": ["TLSv1", "TLSv1.1", "TLSv1.2", "TLSv1.3"]}, "OCSPStapling": {"Switch": "off"}, "HTTP2": {"Switch": "on"}, "QUIC": {"Switch": "off"}, "UpstreamHTTP2": {"Switch": "off"}, "IPv6": {"Switch": "off"}, "WebSocket": {"Switch": "on", "Timeout": 30}, "PostMaxSize": {"Switch": "on", "MaxSize": 838860800}, "ClientIPHeader": {"Switch": "off", "HeaderName": ""}, "ClientIPCountry": {"Switch": "on", "HeaderName": "EO-Client-IPCountry"}, "gRPC": {"Switch": "off"}, "AccelerateMainland": {"Switch": "off"}, "StandardDebug": {"Switch": "on", "AllowClientIPList": ["1.2.3.4"], "Expires": "2023-11-04T04:46:28Z"}}
```

Output: 
```
{
    "Response": {
        "TaskId": "33mz68e4gwka",
        "RequestId": "5e0a2b4e-dw6d-4dsa-ac39-1706cbf8a703"
    }
}
```

**Example 3: 导入站点七层加速配置的规则引擎配置**

单独导入站点 zone-m2kplohsdc4b 下七层加速配置的规则引擎配置。

Input: 

```
tccli teo ImportZoneConfig --cli-unfold-argument  \
    --ZoneId zone-m2kplohsdc4b \
    --Content {"FormatVersion":"1.0","Rules": [{"RuleName": "未命名规则", "Branches": [{"Condition": "${http.request.host} matches ".*"", "Actions": [{"Name": "UpstreamURLRewrite", "Parameters": {"Type": "Path", "Action": "rmvPrefix", "Value": "/prefix"}}], "SubRules": [{"Branches": [{"Condition": "${http.request.file_extension} in [".jpg"]", "Actions": [{"Name": "PostMaxSize", "Parameters": {"Switch": "on", "MaxSize": 524288000}}]}]}, {"Branches": [{"Condition": "${http.request.file_extension} in [".png"]", "Actions": [{"Name": "PostMaxSize", "Parameters": {"Switch": "on", "MaxSize": 209715200}}]}]}]}]}]}
```

Output: 
```
{
    "Response": {
        "TaskId": "33mz68e4gwka",
        "RequestId": "5e0a2b4e-dw6d-4dsa-ac39-1706cbf8a703"
    }
}
```

