**Example 1: 查询日志**

本接口用于查询实例日志

Input: 

```
tccli mongodb DescribeMongodbLogs --cli-unfold-argument  \
    --InstanceId cmgo-k2p5su09 \
    --StartTime 2024-03-07 9:22:15 \
    --EndTime 2024-03-07 15:33:15 \
    --LogComponents NETWORK \
    --LogDetailParams 'client metadata'
```

Output: 
```
{
    "Response": {
        "LogList": [
            {
                "LogComponent": "NETWORK",
                "LogConnection": "conn269939",
                "LogDetail": "{\"t\":{\"$date\":\"2024-03-07T10:29:50.027+08:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":51800,   \"ctx\":\"conn269939\",\"msg\":\"client metadata\",\"attr\":{\"remote\":\"127.0.0.1:39024\",\"client\":\"conn269939\",\"doc\":{\"driver\":{\"name\":\"mongo-go-driver\",\"version\":\"v1.10.6\"},\"os\":{\"type\":\"linux\",\"architecture\":\"amd64\"},\"platform\":\"go1.20.4\",\"application\":{\"name\":\"CMongo\"}}}}",
                "LogId": "51800",
                "LogLevel": "WARNING",
                "LogTime": "2024-03-07T10:29:50.027+08:00"
            }
        ],
        "RequestId": "ab2323tf-rqew1111",
        "TotalCount": 1
    }
}
```

