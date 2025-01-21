**Example 1: 查询操作记录**



Input: 

```
tccli cdwdoris DescribeInstanceOperationHistory --cli-unfold-argument  \
    --InstanceId cdwdoris-xxx \
    --PageNum 1 \
    --PageSize 3 \
    --StartTime 2024-07-28 00:00:00 \
    --EndTime 2025-08-26 17:49:49
```

Output: 
```
{
    "Response": {
        "TotalCount": 66,
        "Operations": [
            {
                "JobId": 14103,
                "Name": "restart_cluster",
                "Desc": "str",
                "Result": "Success",
                "Level": "Normal",
                "LevelDesc": "str",
                "StartTime": "2024-09-11 11:17:31",
                "EndTime": "2024-09-11 11:18:51.523283",
                "ResultDesc": "str",
                "OperateUin": "str",
                "OperationDetail": "str"
            },
            {
                "JobId": 14102,
                "Name": "restart_cluster",
                "Desc": "str",
                "Result": "Success",
                "Level": "Normal",
                "LevelDesc": "str",
                "StartTime": "2024-09-11 11:15:10",
                "EndTime": "2024-09-11 11:17:27.470959",
                "ResultDesc": "str",
                "OperateUin": "str",
                "OperationDetail": "str"
            },
            {
                "JobId": 14101,
                "Name": "restart_cluster",
                "Desc": "str",
                "Result": "Success",
                "Level": "Normal",
                "LevelDesc": "str",
                "StartTime": "2024-09-11 11:13:28",
                "EndTime": "2024-09-11 11:14:07.669157",
                "ResultDesc": "str",
                "OperateUin": "str",
                "OperationDetail": "str"
            }
        ],
        "RequestId": "str-str-str-str-str",
        "Message": ""
    }
}
```

