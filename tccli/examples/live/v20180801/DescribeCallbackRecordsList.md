**Example 1: 请求示例**

用于查询回调事件。

Input: 

```
tccli live DescribeCallbackRecordsList --cli-unfold-argument  \
    --StreamName stream1 \
    --StartTime 2020-10-12T00:00:00+08:00 \
    --EndTime 2020-10-12T00:10:00+08:00 \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "EventTime": "2020-10-12T00:00:00+08:00",
                "EventType": 1,
                "Request": "request body",
                "Response": "response body",
                "ResponseTime": "2020-10-12T00:00:00+08:00",
                "ResultCode": 1,
                "StreamId": "stream1"
            }
        ],
        "PageNum": 1,
        "PageSize": 1,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

