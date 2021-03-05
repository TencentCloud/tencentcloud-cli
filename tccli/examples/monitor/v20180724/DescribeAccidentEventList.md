**Example 1: 获取平台事件列表**

获取平台事件列表

Input: 

```
tccli monitor DescribeAccidentEventList --cli-unfold-argument  \
    --Module monitor
```

Output: 
```
{
    "Response": {
        "Alarms": [
            {
                "OccurTime": "2019-10-10T15:03:31+08:00",
                "BusinessID": 1,
                "AffectResource": "ins-19708ino",
                "EventStatus": 0,
                "Region": "gz",
                "UpdateTime": "2019-10-10T15:03:31+08:00",
                "AccidentTypeDesc": "云服务器运行异常",
                "BusinessTypeDesc": "服务问题"
            }
        ],
        "Total": 1,
        "RequestId": "test813c-45d8-459a-8978-aaasahuiaa"
    }
}
```

