**Example 1: 请求示例**



Input: 

```
tccli live DescribeCallbackRecordsList --cli-unfold-argument  \
    --StreamName test \
    --StartTime 2020-10-12 00:00:00 \
    --EndTime 2020-10-12 00:10:00 \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "PageNum": 1,
        "PageSize": 10,
        "TotalNum": 11,
        "TotalPage": 2,
        "RequestId": "xx",
        "DataInfoList": [
            {
                "EventTime": "2020-10-12 00:32:10",
                "EventType": 0,
                "Request": "opensso++server%3D10.12.1.1%3A",
                "Response": "status+code%3A200%2C+content%3DSuccess",
                "ResponseTime": "2020-10-12 00:32:11",
                "ResultCode": 0,
                "StreamId": "test"
            }
        ]
    }
}
```

