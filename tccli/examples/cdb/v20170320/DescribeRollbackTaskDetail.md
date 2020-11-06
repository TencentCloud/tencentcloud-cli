**Example 1: 查询回档任务详情**



Input: 

```
tccli cdb DescribeRollbackTaskDetail --cli-unfold-argument  \
    --InstanceId cdb-qwer1234 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Items": [
            {
                "Info": "batch rollback success",
                "Status": "SUCCESS",
                "Progress": 100,
                "StartTime": "2020-04-22 10:01:23",
                "EndTime": "2020-04-22 10:06:25",
                "Detail": [
                    {
                        "InstanceId": "cdb-qwer1234",
                        "Strategy": "full",
                        "RollbackTime": "2020-04-22 10:00:57",
                        "Databases": [],
                        "Tables": [
                            {
                                "Table": [
                                    {
                                        "TableName": "sbtest1",
                                        "NewTableName": "sbtest1_bak"
                                    },
                                    {
                                        "TableName": "sbtest2",
                                        "NewTableName": "sbtest2_bak"
                                    }
                                ],
                                "Database": "dbtest_bak"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "1ac120c8-744a-4c15-be4e-4431511c0233"
    }
}
```

