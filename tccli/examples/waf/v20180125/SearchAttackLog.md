**Example 1: 搜索攻击日志详情内容**



Input: 

```
tccli waf SearchAttackLog --cli-unfold-argument  \
    --StartTime 2020-08-2800:00:00 \
    --EndTime 2020-08-2814:12:36 \
    --Domain all \
    --Context xxxxx \
    --QueryString method:GET \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Content": "{\"ipinfo_province\":\"四川\",\"ipinfo_state\":\"CN\",\"attack_type\":\"XSS攻击\",\"ipinfo_city\":\"成都\",\"ipinfo_dimensionality\":\"30.658529\",\"attack_ip\":\"132.232.42.183\",\"uuid\":\"f860aac92f758432779cdf0b5b244266-57538d9b7970dfb5bb222e933d6a2d7d\",\"attack_content\":\"alert()\",\"http_log\":\"\\\"{\\\\\\\"REQUEST_ARG_RAW\\\\\\\":{\\\\\\\"id\\\\\\\":\\\\\\\"alert()\\\\\\\"},\\\\\\\"PROCOTOL\\\\\\\":\\\\\\\"HTTP\\\\\\\\\\\\/1.1\\\\\\\",\\\\\\\"REQEUST_HEADERS_RAW\\\\\\\":\\\\\\\"GET \\\\\\\\\\\\/ HTTP\\\\\\\\\\\\/1.1\\\\\\\\nHost:bj-clbwaf.qcloudwaf.com\\\\\\\\nconnection:close\\\\\\\\ncontent-length:0\\\\\\\\naccept:*\\\\\\\\\\\\/*\\\\\\\\nuser-agent:curl\\\\\\\\\\\\/7.29.0\\\\\\\\n\\\\\\\",\\\\\\\"REQUEST_METHOD\\\\\\\":\\\\\\\"GET\\\\\\\"}\\\"\",\"ipinfo_nation\":\"中国\",\"pan\":\"bj-clbwaf.qcloudwaf.com\",\"user_agent\":\"curl/7.29.0\",\"method\":\"GET\",\"count\":1,\"ipinfo_detail\":\"tencent.com\",\"args_name\":\"ARGS_GET\",\"ipinfo_isp\":\"电信/联通/移动\",\"uri\":\"/\",\"rule_id\":22000002,\"risk_level\":1,\"appid\":1256704386,\"attack_time\":\"2020-08-28 11:07:18\",\"domain\":\"bj-clbwaf.qcloudwaf.com\",\"ipinfo_longitude\":\"104.075546\",\"status\":0}",
                "Source": "",
                "TimeStamp": "2020-08-28 11:07:18"
            },
            {
                "Content": "{\"ipinfo_province\":\"四川\",\"ipinfo_state\":\"CN\",\"attack_type\":\"SQL注入攻击\",\"ipinfo_city\":\"成都\",\"ipinfo_dimensionality\":\"30.658529\",\"attack_ip\":\"132.232.42.183\",\"uuid\":\"ed0ddb4f49236b1a28e0f55c72cee974-145e10f0d70f0a07b6c426acd3ee3341\",\"attack_content\":\"GET /?id= 11 or benchmark(100000000,MD5(1))-- - HTTP/1.1\",\"http_log\":\"\\\"{\\\\\\\"REQUEST_ARG_RAW\\\\\\\":{},\\\\\\\"PROCOTOL\\\\\\\":\\\\\\\"HTTP\\\\\\\\\\\\/1.1\\\\\\\",\\\\\\\"REQEUST_HEADERS_RAW\\\\\\\":\\\\\\\"GET \\\\\\\\\\\\/ HTTP\\\\\\\\\\\\/1.1\\\\\\\\nHost:bj-clbwaf.qcloudwaf.com\\\\\\\\nconnection:close\\\\\\\\nstgw-orgreq:GET \\\\\\\\\\\\/?id= 11 or benchmark(100000000,MD5(1))--+- HTTP\\\\\\\\\\\\/1.1\\\\\\\\naccept:*\\\\\\\\\\\\/*\\\\\\\\ncontent-length:0\\\\\\\\nuser-agent:curl\\\\\\\\\\\\/7.29.0\\\\\\\\n\\\\\\\",\\\\\\\"REQUEST_METHOD\\\\\\\":\\\\\\\"GET\\\\\\\"}\\\"\",\"ipinfo_nation\":\"中国\",\"pan\":\"bj-clbwaf.qcloudwaf.com\",\"user_agent\":\"curl/7.29.0\",\"method\":\"GET\",\"count\":1,\"ipinfo_detail\":\"tencent.com\",\"args_name\":\"REQUEST_HEADERS\",\"ipinfo_isp\":\"电信/联通/移动\",\"uri\":\"/\",\"rule_id\":21000003,\"risk_level\":1,\"appid\":1256704386,\"attack_time\":\"2020-08-28 11:06:07\",\"domain\":\"bj-clbwaf.qcloudwaf.com\",\"ipinfo_longitude\":\"104.075546\",\"status\":0}",
                "Source": "",
                "TimeStamp": "2020-08-28 11:06:07"
            }
        ],
        "Count": 2,
        "Context": "",
        "ListOver": true,
        "SqlFlag": false,
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

