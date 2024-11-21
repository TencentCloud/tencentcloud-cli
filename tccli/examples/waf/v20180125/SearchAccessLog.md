**Example 1: 搜索访问日志**

搜索访问日志

Input: 

```
tccli waf SearchAccessLog --cli-unfold-argument  \
    --TopicId 1ae37c76-df99-4e2b-998c-20f39eba6226 \
    --From 1625395948532 \
    --To 1626000748532 \
    --Query bot:1 \
    --Limit 2 \
    --Context cont \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "Context": "Y29udGV4dC1jMDhiYjAyMy1mMjZmLTQ1NjUtOTEzMy1iZjIwYWUzNmY1MzMxNjI2MTU5NDU4MjQy",
        "ListOver": false,
        "Analysis": false,
        "Results": [
            {
                "PkgLogId": "pkg-log-id",
                "FileName": "name",
                "PkgId": "pkg-id",
                "Source": "src",
                "TopicName": "name",
                "Time": 1625995282703,
                "TopicId": "1ae37c76-df99-4e2b-998c-20f39eba6226",
                "LogJson": "{\"ipinfo_province\":\"共享地址\",\"schema\":\"http\",\"referer\":\"\",\"ipinfo_state\":\"\",\"ipinfo_city\":\"\",\"edition\":\"sparta-waf\",\"ipinfo_dimensionality\":\"\",\"language\":\"\",\"body\":\"\",\"uuid\":\"b285a612f62f5b76478fce8960d2327e-c613c8e835f1d2a48221efa4a21c4247\",\"upstream_status\":\"200\",\"request_time\":\"0.141\",\"content_type\":\"\",\"host\":\"bangskt.qcloudwaf.com\",\"client\":\"100.88.193.73\",\"connection\":\"\",\"ipinfo_nation\":\"共享地址\",\"user_agent\":\"TSecWaf_AccessCheckClient\",\"headers\":\"Accept-Encoding: \",\"upstream\":\"119.29.90.203:80\",\"cookie\":\"\",\"method\":\"GET\",\"query\":\"\",\"ipinfo_detail\":\"\",\"encoding\":\"\",\"ipinfo_isp\":\"\",\"bytes_sent\":\"718\",\"url\":\"/\",\"accept\":\"\",\"x_forwarded_for\":\"\",\"upstream_connect_time\":\"0.036\",\"request_length\":\"86\",\"appid\":\"251011484\",\"domain\":\"bangskt.qcloudwaf.com\",\"msec\":\"1625995282.703\",\"upstream_response_time\":\"0.068\",\"time\":\"11/Jul/2021:17:21:22 +0800\",\"ipinfo_longitude\":\"\",\"status\":\"200\"}"
            }
        ],
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

