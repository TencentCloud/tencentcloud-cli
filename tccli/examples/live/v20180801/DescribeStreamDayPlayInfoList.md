**Example 1: 请求示例**



Input: 

```
tccli live DescribeStreamDayPlayInfoList --cli-unfold-argument  \
    --PlayDomain 5000.livepush.com \
    --DayTime 2019-02-21 \
    --PageNum 1 \
    --PageSize 1000
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "StreamName": "test1",
                "TotalFlux": 500.0
            }
        ],
        "TotalNum": 100,
        "TotalPage": 1,
        "PageNum": 1,
        "PageSize": 1000,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

