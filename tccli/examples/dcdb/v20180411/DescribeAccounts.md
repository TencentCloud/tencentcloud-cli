**Example 1: 获取实例账号信息**



Input: 

```
tccli dcdb DescribeAccounts --cli-unfold-argument  \
    --InstanceId tdsqlshard-jsn16bwh
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsqlshard-jsn16bwh",
        "RequestId": "63b981d8-157c-436a-b8d9-4f401fc3e435",
        "Users": [
            {
                "CreateTime": "2025-03-18 12:39:36",
                "DelayThresh": 0,
                "Description": "",
                "Host": "%",
                "MaxUserConnections": 0,
                "ReadOnly": 0,
                "SlaveConst": 0,
                "UpdateTime": "2025-03-18 12:40:09",
                "UserName": "qt4s_test"
            }
        ]
    }
}
```

