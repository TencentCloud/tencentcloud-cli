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
                "Uin": "xx",
                "Event": "xx",
                "Limit": 0,
                "Status": 0,
                "BeginTime": "xx",
                "EndTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

