**Example 1: 请求示例**



Input: 

```
tccli live DescribeDeliverLogDownList --cli-unfold-argument  \
    --StartTime 2022-02-09T12:36:42Z \
    --EndTime 2022-02-09T13:36:42Z \
    --DeliverDomains 5000.liveplay.com
```

Output: 
```
{
    "Response": {
        "LogInfoList": [
            {
                "LogName": "mylog",
                "LogUrl": "https://livelog-down.cdn.qcloud.com/20220804/11/202208041125-pul",
                "LogTime": "2022-02-09T12:36:42Z",
                "FileSize": 0
            }
        ],
        "TotalNum": 1,
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

