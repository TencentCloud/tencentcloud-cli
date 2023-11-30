**Example 1: 获取告警状态示例**

获取告警状态

Input: 

```
tccli weilingwith DescribeAlarmStatusList --cli-unfold-argument  \
    --ApplicationToken RQ7wnN7IMDutqe0JJ6t4MTqbBAePbryn \
    --WorkspaceId 1124
```

Output: 
```
{
    "Response": {
        "RequestId": "257e0b36-70c5-4f51-ac81-83fca0ae7522",
        "Result": {
            "List": [
                {
                    "StatusID": "test",
                    "StatusName": "测试",
                    "StatusType": ""
                }
            ]
        }
    }
}
```

