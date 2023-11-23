**Example 1: 查询版本详情**

查询 ZoneId 为 zone-m2kplohsdc4b 的站点下 VersionId 为 ver-5ksglmhghsu3 的版本详情信息。

Input: 

```
tccli teo DescribeConfigGroupVersionDetail --cli-unfold-argument  \
    --ZoneId zone-m2kplohsdc4b \
    --VersionId ver-5ksglmhghsu3
```

Output: 
```
{
    "Response": {
        "Content": "{\n  \"FormatVersion\": \"1.0\",\n  \"ZoneConfig\": {\n    \"SmartRouting\": {\n      \"Switch\": \"off\"\n    },\n    \"Cache\": {\n      \"CustomTime\": {\n        \"Switch\": \"on\",\n        \"CacheTime\": 604800\n      }\n    },\n    \"MaxAge\": {\n      \"FollowOrigin\": \"on\",\n      \"CacheTime\": 600\n    },\n    \"CacheKey\": {\n      \"FullURLCache\": \"off\",\n      \"QueryString\": {\n        \"Switch\": \"on\",\n        \"Action\": \"includeCustom\",\n        \"Values\": [\n          \"key1\",\n          \"key2\"\n        ]\n      },\n      \"IgnoreCase\": \"on\"\n    },\n    \"CachePrefresh\": {\n      \"Switch\": \"off\",\n      \"CacheTimePercent\": 90\n    },\n    \"OfflineCache\": {\n      \"Switch\": \"on\"\n    },\n    \"Compression\": {\n      \"Switch\": \"on\",\n      \"Algorithms\": [\n        \"brotli\",\n        \"gzip\"\n      ]\n    },\n    \"ImageOptimize\": {\n      \"Switch\": \"off\"\n    },\n    \"ForceRedirectHTTPS\": {\n      \"Switch\": \"on\",\n      \"RedirectStatusCode\": 302\n    },\n    \"HSTS\": {\n      \"Switch\": \"on\",\n      \"IncludeSubDomains\": \"on\",\n      \"Timeout\": 16070400,\n      \"Preload\": \"on\"\n    },\n    \"TLSConfig\": {\n      \"CipherSuite\": \"loose-v2023\",\n      \"Version\": [\n        \"TLSv1\",\n        \"TLSv1.1\",\n        \"TLSv1.2\",\n        \"TLSv1.3\"\n      ]\n    },\n    \"OCSPStapling\": {\n      \"Switch\": \"off\"\n    },\n    \"HTTP2\": {\n      \"Switch\": \"on\"\n    },\n    \"QUIC\": {\n      \"Switch\": \"off\"\n    },\n    \"UpstreamHTTP2\": {\n      \"Switch\": \"off\"\n    },\n    \"IPv6\": {\n      \"Switch\": \"off\"\n    },\n    \"WebSocket\": {\n      \"Switch\": \"on\",\n      \"Timeout\": 30\n    },\n    \"PostMaxSize\": {\n      \"Switch\": \"on\",\n      \"MaxSize\": 838860800\n    },\n    \"ClientIPHeader\": {\n      \"Switch\": \"off\",\n      \"HeaderName\": \"\"\n    },\n    \"ClientIPCountry\": {\n      \"Switch\": \"on\",\n      \"HeaderName\": \"EO-Client-IPCountry\"\n    },\n    \"gRPC\": {\n      \"Switch\": \"off\"\n    },\n    \"AccelerateMainland\": {\n      \"Switch\": \"off\"\n    },\n    \"StandardDebug\": {\n      \"Switch\": \"on\",\n      \"AllowClientIPList\": [\n        \"1.2.3.4\"\n      ],\n      \"Expires\": \"2023-11-04T04:46:28Z\"\n    }\n  },\n  \"Rules\": [\n    {\n      \"RuleName\": \"未命名规则\",\n      \"Branches\": [\n        {\n          \"Condition\": \"${http.request.host} matches '.*'\",\n          \"Actions\": [\n            {\n              \"Name\": \"UpstreamURLRewrite\",\n              \"Parameters\": {\n                \"Type\": \"Path\",\n                \"Action\": \"rmvPrefix\",\n                \"Value\": \"/prefix\"\n              }\n            }\n          ],\n          \"SubRules\": [\n            {\n              \"Branches\": [\n                {\n                  \"Condition\": \"${http.request.file_extension} in ['.jpg']\",\n                  \"Actions\": [\n                    {\n                      \"Name\": \"PostMaxSize\",\n                      \"Parameters\": {\n                        \"Switch\": \"on\",\n                        \"MaxSize\": 524288000\n                      }\n                    }\n                  ]\n                }\n              ]\n            },\n            {\n              \"Branches\": [\n                {\n                  \"Condition\": \"${http.request.file_extension} in ['.png']\",\n                  \"Actions\": [\n                    {\n                      \"Name\": \"PostMaxSize\",\n                      \"Parameters\": {\n                        \"Switch\": \"on\",\n                        \"MaxSize\": 209715200\n                      }\n                    }\n                  ]\n                }\n              ]\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}",
        "ConfigGroupVersionInfo": {
            "CreateTime": "2023-11-06T11:33:12Z",
            "Description": "test",
            "GroupId": "cg-2p9unsmt54uw",
            "GroupType": "l7_acceleration",
            "Status": "inactive",
            "VersionId": "ver-2pn240kqwgti",
            "VersionNumber": "1"
        },
        "RequestId": "9bd9c732-8f9a-4cd3-a3e8-1c9db5e53631"
    }
}
```

