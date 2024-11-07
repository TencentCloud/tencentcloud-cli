**Example 1: 获取告警策略**

获取告警策略

Input: 

```
tccli cloudhsm GetAlarmEvent --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AlarmConfig": [
            {
                "BeginTime": "01:00:00",
                "EndTime": "01:59:59",
                "Event": "MEM",
                "Limit": 0,
                "Status": 1,
                "Uin": "22234567"
            },
            {
                "BeginTime": "01:00:00",
                "EndTime": "01:59:59",
                "Event": "CPU",
                "Limit": 1,
                "Status": 1,
                "Uin": "22234567"
            },
            {
                "BeginTime": "01:00:00",
                "EndTime": "01:59:59",
                "Event": "TCP",
                "Limit": 99,
                "Status": 1,
                "Uin": "22234567"
            }
        ],
        "RequestId": "2045f89b-7673-4cd7-9580-77f0a048fb26"
    }
}
```

