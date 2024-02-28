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
                "BeginTime": "",
                "EndTime": "",
                "Event": "MEM",
                "Limit": 0,
                "Status": 1,
                "Uin": "123456789"
            },
            {
                "BeginTime": "",
                "EndTime": "",
                "Event": "CPU",
                "Limit": 1,
                "Status": 1,
                "Uin": "123456789"
            },
            {
                "BeginTime": "",
                "EndTime": "",
                "Event": "TCP",
                "Limit": 99,
                "Status": 1,
                "Uin": "123456789"
            }
        ],
        "RequestId": "2045f89b-7673-4cd7-9580-77f0a048fb26"
    }
}
```

