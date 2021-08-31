**Example 1: 告警设置-获取当前用户修改的告警列表**

告警设置-获取当前用户修改的告警列表

Input: 

```
tccli cwp DescribeWarningList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "WarningInfoList": [
            {
                "Type": 3,
                "DisablePhoneWarning": 1,
                "BeginTime": "00:00",
                "EndTime": "23:23",
                "TimeZone": "Asia/Shanghai",
                "ControlBit": 0,
                "ControlBits": "000"
            },
            {
                "Type": 9,
                "DisablePhoneWarning": 1,
                "BeginTime": "10:00",
                "EndTime": "23:23",
                "TimeZone": "Asia/Shanghai",
                "ControlBit": 7,
                "ControlBits": "111"
            },
            {
                "Type": 4,
                "DisablePhoneWarning": 1,
                "BeginTime": "01:00",
                "EndTime": "23:23",
                "TimeZone": "Asia/Shanghai",
                "ControlBit": 0,
                "ControlBits": "000"
            }
        ]
    }
}
```

