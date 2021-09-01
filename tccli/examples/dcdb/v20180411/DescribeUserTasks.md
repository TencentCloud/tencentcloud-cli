**Example 1: 拉取用户任务列表**



Input: 

```
tccli dcdb DescribeUserTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 6,
        "RequestId": "136034",
        "FlowSet": [
            {
                "Status": 2,
                "InstanceId": "tdsqlshard-d7tnnu13",
                "RegionId": 1,
                "InputData": "{\"AppId\":1251664966,\"UserType\":1,\"Uin\":\"1410643447\",\"Operator\":\"1410643447\",\"Ids\":[10182],\"RetreatedTime\":\"2016-02-18 04:01:40\"}",
                "CreateTime": "2016-03-17 16:08:10",
                "AppId": 251000022,
                "UserTaskType": 0,
                "EndTime": "2016-03-17 16:10:48",
                "InstanceName": "tdsqlshard-d7tnnu13",
                "Id": 23,
                "ErrMsg": ""
            },
            {
                "Status": 2,
                "InstanceId": "tdsqlshard-d7tnnu13",
                "RegionId": 1,
                "InputData": "{\"AppId\":1251664966,\"UserType\":1,\"Uin\":\"1410643447\",\"Operator\":\"1410643447\",\"Ids\":[10182],\"RetreatedTime\":\"2016-02-11 01:21:37\"}",
                "CreateTime": "2016-03-10 20:57:05",
                "AppId": 251000022,
                "UserTaskType": 0,
                "EndTime": "2016-03-10 20:59:09",
                "InstanceName": "tdsqlshard-d7tnnu13",
                "Id": 22,
                "ErrMsg": ""
            },
            {
                "Status": 2,
                "InstanceId": "tdsqlshard-7aqf6abn",
                "RegionId": 1,
                "InputData": "{\"AppId\":1251664966,\"UserType\":1,\"Uin\":\"1410643447\",\"Operator\":\"1410643447\",\"Ids\":[10182],\"RetreatedTime\":\"2016-02-18 01:21:37\"}",
                "CreateTime": "2016-03-10 19:19:54",
                "AppId": 251000022,
                "UserTaskType": 0,
                "EndTime": "2016-03-10 19:22:54",
                "InstanceName": "tdsqlshard-7aqf6abn",
                "Id": 21,
                "ErrMsg": ""
            },
            {
                "Status": 3,
                "InstanceId": "tdsqlshard-7aqf6abn",
                "RegionId": 1,
                "InputData": "{\"AppId\":1251664966,\"UserType\":1,\"Uin\":\"1410643447\",\"Operator\":\"1410643447\",\"Ids\":[10160],\"RetreatedTime\":\"2016-01-01 01:30:30\"}",
                "CreateTime": "2016-01-29 18:14:44",
                "AppId": 251000022,
                "UserTaskType": 0,
                "EndTime": "2016-01-29 18:22:13",
                "InstanceName": "tdsqlshard-7aqf6abn",
                "Id": 18,
                "ErrMsg": "pickValidBinlog error"
            },
            {
                "Status": 3,
                "InstanceId": "tdsqlshard-7aqf6abn",
                "RegionId": 1,
                "InputData": "{\"AppId\":1251664966,\"UserType\":1,\"Uin\":\"1410643447\",\"Operator\":\"1410643447\",\"Ids\":[10160],\"RetreatedTime\":\"2015-12-30 03:48:33\"}",
                "CreateTime": "2016-01-18 20:01:47",
                "AppId": 251000022,
                "UserTaskType": 0,
                "EndTime": "2016-01-18 20:09:16",
                "InstanceName": "tdsqlshard-7aqf6abn",
                "Id": 16,
                "ErrMsg": "pickValidBinlog error"
            },
            {
                "Status": 3,
                "InstanceId": "tdsqlshard-7aqf6abn",
                "RegionId": 1,
                "InputData": "{\"AppId\":1251664966,\"UserType\":1,\"Uin\":\"1410643447\",\"Operator\":\"1410643447\",\"Ids\":[10160],\"RetreatedTime\":\"2015-12-29 03:48:33\"}",
                "CreateTime": "2016-01-18 19:37:18",
                "AppId": 251000022,
                "UserTaskType": 0,
                "EndTime": "2016-01-18 19:44:47",
                "InstanceName": "tdsqlshard-7aqf6abn",
                "Id": 15,
                "ErrMsg": "pickValidBinlog error"
            }
        ]
    }
}
```

