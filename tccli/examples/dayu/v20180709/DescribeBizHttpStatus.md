**Example 1: 获取业务流量状态码统计曲线**



Input: 

```
tccli dayu DescribeBizHttpStatus --cli-unfold-argument  \
    --Domain xx \
    --Statistics xx \
    --Business xx \
    --ProtoInfo.0.Protocol xx \
    --ProtoInfo.0.Port 1 \
    --Period 1 \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --Id xx
```

Output: 
```
{
    "Response": {
        "HttpStatusMap": {
            "SourceHttp2xx": [
                1,
                2,
                3,
                2
            ],
            "Http5xx": [
                1,
                2,
                3,
                2
            ],
            "SourceHttp5xx": [
                1,
                2,
                3,
                2
            ],
            "SourceHttp404": [
                1,
                2,
                3,
                2
            ],
            "Http4xx": [
                1,
                2,
                3,
                2
            ],
            "SourceHttp4xx": [
                1,
                2,
                3,
                2
            ],
            "Http2xx": [
                1,
                2,
                3,
                2
            ],
            "Http404": [
                1,
                2,
                3,
                2
            ],
            "SourceHttp3xx": [
                1,
                2,
                3,
                2
            ],
            "Http3xx": [
                1,
                2,
                3,
                2
            ]
        },
        "RequestId": "xx"
    }
}
```

