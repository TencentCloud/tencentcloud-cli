**Example 1: 瀑布图响应示例**



Input: 

```
tccli cat DescribeChartDetail --cli-unfold-argument  \
    --ProbeTime 1645498961000 \
    --ChartType domainpie \
    --TaskID task-rjdpau6y \
    --TaskType AnalyzeTaskType_Browse
```

Output: 
```
{
    "Response": {
        "ChartDetails": [],
        "PieDetails": [
            {
                "Index": 1,
                "Domain": "baidu.com",
                "MimeType": "",
                "ElementNum": 1,
                "ErrElementNum": 0,
                "BytesReceived": 0,
                "TotalTime": 0.141,
                "ElementUseable": 100,
                "Cname": "baidu.com"
            },
            {
                "Index": 2,
                "Domain": "sp1.baidu.com",
                "MimeType": "",
                "ElementNum": 1,
                "ErrElementNum": 0,
                "BytesReceived": 0.341,
                "TotalTime": 0.266,
                "ElementUseable": 100,
                "Cname": "www.a.shifen.com:sp1.baidu.com"
            },
            {
                "Index": 3,
                "Domain": "sp2.baidu.com",
                "MimeType": "",
                "ElementNum": 1,
                "ErrElementNum": 0,
                "BytesReceived": 0.341,
                "TotalTime": 0.41,
                "ElementUseable": 100,
                "Cname": "www.a.shifen.com:sp2.baidu.com"
            },
            {
                "Index": 4,
                "Domain": "passport.baidu.com",
                "MimeType": "",
                "ElementNum": 1,
                "ErrElementNum": 0,
                "BytesReceived": 2.424,
                "TotalTime": 0.562,
                "ElementUseable": 100,
                "Cname": "passport.n.shifen.com:passport.baidu.com"
            },
            {
                "Index": 5,
                "Domain": "hectorstatic.baidu.com",
                "MimeType": "",
                "ElementNum": 1,
                "ErrElementNum": 0,
                "BytesReceived": 56.73,
                "TotalTime": 0.668,
                "ElementUseable": 100,
                "Cname": "opencdnbd.jomodns.com:hectorstatic.baidu.com:hectorstatic.baidu.com.a.bdydns.com"
            },
            {
                "Index": 6,
                "Domain": "www.baidu.com",
                "MimeType": "",
                "ElementNum": 7,
                "ErrElementNum": 0,
                "BytesReceived": 151.858,
                "TotalTime": 1.38,
                "ElementUseable": 100,
                "Cname": "www.a.shifen.com:www.baidu.com"
            },
            {
                "Index": 7,
                "Domain": "pss.bdstatic.com",
                "MimeType": "",
                "ElementNum": 10,
                "ErrElementNum": 0,
                "BytesReceived": 248.125,
                "TotalTime": 1.58,
                "ElementUseable": 100,
                "Cname": "opencdnglobalv6.jomodns.com:pss.bdstatic.com:pss.bdstatic.com.a.bdydns.com"
            },
            {
                "Index": 8,
                "Domain": "dss0.bdstatic.com",
                "MimeType": "",
                "ElementNum": 31,
                "ErrElementNum": 0,
                "BytesReceived": 300.396,
                "TotalTime": 1.728,
                "ElementUseable": 100,
                "Cname": "sslbaiduv6.jomodns.com:dss0.bdstatic.com"
            }
        ],
        "RequestId": "db809307-03b1-4675-9cde-8b4034a64d37"
    }
}
```

**Example 2: 查询页面性能瀑布图，TCP连接图，饼图请求示例**



Input: 

```
tccli cat DescribeChartDetail --cli-unfold-argument  \
    --City aa \
    --Operators aa \
    --Districts aa \
    --ProbeTime 1 \
    --TaskID aa \
    --TaskType aa \
    --ChartType aa
```

Output: 
```
{
    "Response": {
        "PieDetails": [
            {
                "MimeType": "aa",
                "Index": 1,
                "Domain": "aa",
                "ElementUseable": 0,
                "BytesReceived": 0,
                "ElementNum": 0,
                "Cname": "aa",
                "ErrElementNum": 0,
                "TotalTime": 0
            }
        ],
        "RequestId": "aa",
        "ChartDetails": [
            {
                "TotalTime": 0,
                "Index": 1,
                "SslTime": 0,
                "RequestTime": 0,
                "MimeType": "aa",
                "ResponseTime": 0,
                "Method": "aa",
                "TcpNum": 1,
                "URL": "aa",
                "StatMainID": 1,
                "DownloadTime": 0,
                "BlockTime": 0,
                "VeName": "aa",
                "TcpTime": 0,
                "StartTime": 0,
                "TargetIP": "aa",
                "HttpVersion": "aa",
                "DnsTime": 0,
                "DownloadSize": 0,
                "MonitorTime": "aa",
                "StatusCode": 1
            }
        ]
    }
}
```

