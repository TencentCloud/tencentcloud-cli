**Example 1: 查询日志分析日志详情**

查询 ID 为 “zone-2z55fgysdtmc” 的站点下，归属地区为中国大陆境内北京时间 2025-07-10 00:00:00 ～ 2025-07-11 00:00:00 之间的七层访问日志数据详情，按时间倒序。
日志匹配条件：请求域名为"www.example.com"，并且命中状态为“命中”或"未命中"。

Input: 

```
tccli teo DescribeLogAnalysisDetail --cli-unfold-argument  \
    --ZoneId zone-2z55fgysdtmc \
    --Area mainland \
    --StartTime 2025-07-10T00:00:00+08:00 \
    --EndTime 2025-07-11T00:00:00+08:00 \
    --LogType l7-access-logs \
    --Condition ${RequestHost} in ['www.example.com'] AND ${EdgeCacheStatus} in ['hit','miss'] \
    --Limit 100 \
    --Offset 0 \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "RequestId": "88e4f1a4-ee44-42e9-8aa8-a9b1631ecc5e",
        "LogDetail": [
            {
                "Timestamp": 1752137534000,
                "LogJson": "{\"RequestID\":\"13719873400581239472\",\"RequestSSLProtocol\":\"-\",\"RequestScheme\":\"HTTPS\",\"LogTime\":\"2025-07-10T08:52:14Z\",\"EdgeResponseStatusCode\":404,\"ClientIP\":\"0.0.0.0\",\"RequestHost\":\"www.example.com\",\"RequestProtocol\":\"HTTP/1.1\",\"EdgeCacheStatus\": \"hit\",\"RequestUA\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"EdgeServerIP\":\"0.0.0.0\"}"
            },
            {
                "Timestamp": 1752135679000,
                "LogJson": "{\"RequestID\":\"13719873400528347025\",\"RequestSSLProtocol\":\"-\",\"RequestScheme\":\"HTTPS\",\"LogTime\":\"2025-07-10T08:21:19Z\",\"EdgeResponseStatusCode\":200,\"ClientIP\":\"0.0.0.0\",\"RequestHost\":\"www.example.com\",\"RequestProtocol\":\"HTTP/1.1\",\"EdgeCacheStatus\": \"hit\",\"RequestUA\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"EdgeServerIP\":\"0.0.0.0\"}"
            },
            {
                "Timestamp": 1752134456000,
                "LogJson": "{\"RequestID\":\"13719873400520394827\",\"RequestSSLProtocol\":\"-\",\"RequestScheme\":\"HTTPS\",\"LogTime\":\"2025-07-10T08:00:56Z\",\"EdgeResponseStatusCode\":200,\"ClientIP\":\"0.0.0.0\",\"RequestHost\":\"www.example.com\",\"RequestProtocol\":\"HTTP/1.1\",\"EdgeCacheStatus\": \"hit\",\"RequestUA\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"EdgeServerIP\":\"0.0.0.0\"}"
            },
            {
                "Timestamp": 1752131866310,
                "LogJson": "{\"RequestID\":\"13719873400524368235\",\"RequestSSLProtocol\":\"-\",\"RequestScheme\":\"HTTPS\",\"LogTime\":\"2025-07-10T07:16:40Z\",\"EdgeResponseStatusCode\":200,\"ClientIP\":\"0.0.0.0\",\"RequestHost\":\"www.example.com\",\"RequestProtocol\":\"HTTP/1.1\",\"EdgeCacheStatus\": \"hit\",\"RequestUA\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"EdgeServerIP\":\"0.0.0.0\"}"
            }
        ],
        "TotalCount": 4
    }
}
```

