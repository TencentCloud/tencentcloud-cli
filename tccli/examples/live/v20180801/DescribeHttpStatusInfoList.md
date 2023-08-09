**Example 1: 请求示例**



Input: 

```
tccli live DescribeHttpStatusInfoList --cli-unfold-argument  \
    --EndTime 2019-03-01T00:01:00+08:00 \
    --StartTime 2019-03-01T00:00:00+08:00 \
    --PlayDomains 5000.liveplay.com
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01T00:00:00+08:00",
                "HttpStatusInfoList": [
                    {
                        "HttpStatus": "200",
                        "Num": 100
                    }
                ]
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

