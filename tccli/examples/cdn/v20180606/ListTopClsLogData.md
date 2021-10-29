**Example 1: 通过CLS日志计算Top信息**



Input: 

```
tccli cdn ListTopClsLogData --cli-unfold-argument  \
    --Channel cdn \
    --LogsetId 4242424-8723-45e3-9c75-a0599ef9143a \
    --TopicIds 57460798-8723-45e3-9c75-a0599ef9143a,57460798-8723-45e3-9c75-22242141 \
    --StartTime '2019-11-18 00:00:00' \
    --EndTime '2019-11-18 00:10:00' \
    --Domain www.test.com \
    --Url /abc/123.jpg \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "242144aeff-8723-45e3-9c75-a0599ef9143a",
        "Data": [
            {
                "ClientIp": "1.1.1.1",
                "Time": "2019-11-18 00:00:00",
                "Request": 300,
                "Count": "2"
            },
            {
                "ClientIp": "2.2.2.2",
                "Time": "2019-11-18 00:00:01",
                "Request": 200,
                "Count": "1"
            }
        ],
        "TotalCount": 3,
        "IpCount": 2
    }
}
```

