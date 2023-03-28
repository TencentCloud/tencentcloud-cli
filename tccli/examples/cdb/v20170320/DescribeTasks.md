**Example 1: 查询云数据库实例任务列表**

查询云数据库实例任务列表

Input: 

```
tccli cdb DescribeTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 5,
        "Items": [
            {
                "Code": 9013,
                "Message": "[Operate CDB Fail][Upgrade Service Fail!] reason: ERR#-999: lock_inst.cgi: 某些实例id不存在对应的实例记录",
                "JobId": 79,
                "AsyncRequestId": "9d21004b-3aa1896a-eeddca4b-a68f106d",
                "Progress": 10,
                "StartTime": "2019-10-09 20:03:39",
                "EndTime": "2019-10-09 20:39:34",
                "InstanceIds": [
                    "cdb-qlfpnobr"
                ],
                "TaskType": "OPEN GTID",
                "TaskStatus": "FAILED"
            },
            {
                "Code": 0,
                "Message": "设置参数成功",
                "JobId": 70,
                "AsyncRequestId": "1d564380-2e391736-f28fa246-43cea3aa",
                "Progress": 100,
                "StartTime": "2018-07-06 22:03:05",
                "EndTime": "2018-07-06 22:03:28",
                "InstanceIds": [
                    "cdb-6kd9h71i"
                ],
                "TaskType": "MODIFY PARAM",
                "TaskStatus": "SUCCEED"
            },
            {
                "Code": 0,
                "Message": "初始化实例成功",
                "JobId": 69,
                "AsyncRequestId": "ea39295d-420a0b4e-a98298c7-8751e1ad",
                "Progress": 100,
                "StartTime": "2018-07-06 22:01:42",
                "EndTime": "2018-07-06 22:02:26",
                "InstanceIds": [
                    "cdb-6kd9h71i"
                ],
                "TaskType": "INITIAL",
                "TaskStatus": "SUCCEED"
            },
            {
                "Code": 0,
                "Message": "实例升级任务完成",
                "JobId": 68,
                "AsyncRequestId": "",
                "Progress": 100,
                "StartTime": "2018-07-05 23:53:48",
                "EndTime": "2018-07-06 22:05:10",
                "InstanceIds": [
                    "cdb-6kd9h71i"
                ],
                "TaskType": "UPGRADE MASTER",
                "TaskStatus": "SUCCEED"
            },
            {
                "Code": -1,
                "Message": "设置参数失败",
                "JobId": 66,
                "AsyncRequestId": "780b2e32-79cb0f4c-ec7854c5-44ff5371",
                "Progress": 0,
                "StartTime": "2018-07-05 23:30:36",
                "EndTime": "2018-07-05 23:30:37",
                "InstanceIds": [
                    "cdb-o02fxj9g"
                ],
                "TaskType": "MODIFY PARAM",
                "TaskStatus": "FAILED"
            }
        ],
        "RequestId": "9a4b22f5-0f93-4a72-ba05-1eb6cdf37a1e"
    }
}
```

