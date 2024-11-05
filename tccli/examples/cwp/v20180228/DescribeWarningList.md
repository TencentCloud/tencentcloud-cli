**Example 1: 告警设置-获取当前用户修改的告警列表**

告警设置-获取当前用户修改的告警列表

Input: 

```
tccli cwp DescribeWarningList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-1002",
        "WarningInfoList": [
            {
                "Type": 3,
                "DisablePhoneWarning": 1,
                "BeginTime": "00:00",
                "EndTime": "23:23",
                "TimeZone": "Asia/Shanghai",
                "ControlBit": 0,
                "ControlBits": "000",
                "HostRange": 0,
                "Count": 102
            }
        ]
    }
}
```

