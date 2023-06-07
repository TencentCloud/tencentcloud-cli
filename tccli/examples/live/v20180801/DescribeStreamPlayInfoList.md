**Example 1: 请求示例**

查询流的播放信息列表

Input: 

```
tccli live DescribeStreamPlayInfoList --cli-unfold-argument  \
    --PlayDomain 5000.playdomain.com \
    --StreamName stream1 \
    --EndTime 2019-03-01T00:03:00+08:00 \
    --StartTime 2019-03-01T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01T00:00:00+08:00",
                "Bandwidth": 10.0,
                "Flux": 75.0,
                "Request": 50,
                "Online": 10
            },
            {
                "Time": "2019-03-01T00:02:00+08:00",
                "Bandwidth": 20.0,
                "Flux": 150.0,
                "Request": 50,
                "Online": 20
            },
            {
                "Time": "2019-03-01T00:03:00+08:00",
                "Bandwidth": 30.0,
                "Flux": 225.0,
                "Request": 50,
                "Online": 30
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

