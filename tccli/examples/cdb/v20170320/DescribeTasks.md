**Example 1: Querying task list for TencentDB instance**



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
                "Message": "[Operate CDB Fail][Upgrade Service Fail!] reason: ERR#-999: lock_inst.cgi: no instance records exist for some instance IDs",
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
                "Message": "Set parameter successfully",
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
                "Message": "Initialized instance successfully",
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
                "Message": "Instance upgrade task is completed",
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
                "Message": "Failed to set parameters",
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

