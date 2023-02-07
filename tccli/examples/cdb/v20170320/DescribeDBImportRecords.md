**Example 1: 查询数据库导入任务记录**



Input: 

```
tccli cdb DescribeDBImportRecords --cli-unfold-argument  \
    --InstanceId cdb-7r8h0h61 \
    --EndTime 2017-08-24 15:03:01 \
    --StartTime 2016-01-01 00:00:01
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": "4",
        "Items": [
            {
                "Status": 3,
                "Code": 1,
                "CostTime": 0,
                "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
                "WorkId": "1649290",
                "FileName": "monkey_1501490864.sql",
                "Process": 5,
                "CreateTime": "2017-11-09 14:26:31",
                "FileSize": 12,
                "Message": "lock_inst.cgi: 某些实例id不存在对应的实例记录",
                "JobId": 16242,
                "DbName": "test",
                "AsyncRequestId": "a4788d0a-df23758a-ac961e5a-af414d33"
            },
            {
                "Status": 3,
                "Code": 1,
                "CostTime": 0,
                "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
                "WorkId": "1545387",
                "FileName": "monkey_1501490864.sql",
                "Process": 5,
                "CreateTime": "2017-10-18 21:18:26",
                "FileSize": "12",
                "Message": "lock_inst.cgi: 某些实例id不存在对应的实例记录",
                "JobId": 16223,
                "DbName": "",
                "AsyncRequestId": "198e97de-972b1971-fb0ce76a-08ca054e"
            },
            {
                "Status": 3,
                "Code": 1,
                "CostTime": 0,
                "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
                "WorkId": "1545171",
                "FileName": "monkey_1501490864.sql",
                "Process": 5,
                "CreateTime": "2017-10-18 20:12:07",
                "FileSize": "2",
                "Message": "lock_inst.cgi: 某些实例id不存在对应的实例记录",
                "JobId": 16222,
                "DbName": "test",
                "AsyncRequestId": "9706dfbf-0d1bc6df-5f18f4e1-bb86f2f4"
            },
            {
                "Status": 3,
                "Code": 1,
                "CostTime": 0,
                "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
                "WorkId": "2228867",
                "FileName": "monkey_1501490864.sql",
                "Process": 5,
                "CreateTime": "2017-10-18 17:53:54",
                "FileSize": "12",
                "Message": "lock_inst.cgi: 某些实例id不存在对应的实例记录",
                "JobId": 16209,
                "DbName": "",
                "AsyncRequestId": "e8713d1e-10628d32-74682eef-d0855c1a"
            }
        ]
    }
}
```

