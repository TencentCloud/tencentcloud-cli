**Example 1: 通过检索条件，查询实例慢日志**



Input: 

```
tccli cdb DescribeSlowLogData --cli-unfold-argument  \
    --OrderBy DESC \
    --UserNames usename0 \
    --InstanceId cdb-c1nl9rpv \
    --DataBases database0 \
    --Offset 0 \
    --Limit 400 \
    --SortBy RowsSent \
    --StartTime 1585142640 \
    --UserHosts userhosts0 \
    --EndTime 1585142640
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "Database": "1231231",
                "LockTime": 1,
                "Md5": "23123123",
                "QueryTime": 100,
                "RowsExamined": 0,
                "RowsSent": 0,
                "SqlTemplate": "show master status111111",
                "SqlText": "update order_logistics set logistics_status = 205 where logistics_id in ( select `logistics_id` from `order_info` where order_no in('15706082880074381752', '15706082880074381751'))",
                "Timestamp": 1585142640,
                "UserHost": "localhost",
                "UserName": "marchzcma"
            }
        ]
    }
}
```

