**Example 1: 查询设备操作日志**



Input: 

```
tccli bm DescribeDeviceOperationLog --cli-unfold-argument  \
    --InstanceId cpm-xxx \
    --StartTime 2018-09-05 \
    --EndTime 2018-10-05 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "DeviceOperationLogSet": [
            {
                "Id": 8818,
                "InstanceId": "cpm-xxx",
                "TaskId": 902540,
                "TaskName": "runUserCmd",
                "TaskDescription": "运行用户自定义命令",
                "StartTime": "2018-09-20 17:42:21",
                "EndTime": "2018-09-20 17:42:21",
                "Status": 0,
                "OpUin": "",
                "LogDescription": "运行用户自定义命令"
            },
            {
                "Id": 8816,
                "InstanceId": "cpm-xxx",
                "TaskId": 902536,
                "TaskName": "resetPasswd",
                "TaskDescription": "重置密码",
                "StartTime": "2018-09-20 17:41:39",
                "EndTime": "2018-09-20 17:41:39",
                "Status": 1,
                "OpUin": "1307774067",
                "LogDescription": "重置密码"
            },
            {
                "Id": 8815,
                "InstanceId": "cpm-xxx",
                "TaskId": 0,
                "TaskName": "modifyAlias",
                "TaskDescription": "改名",
                "StartTime": "2018-09-20 17:32:48",
                "EndTime": "2018-09-20 17:32:48",
                "Status": 1,
                "OpUin": "1307774067",
                "LogDescription": "修改设备名称为'melo重启失败'"
            }
        ],
        "TotalCount": 3,
        "RequestId": "d33ccd5a-bda3-498d-994f-98eb3e7380ef"
    }
}
```

