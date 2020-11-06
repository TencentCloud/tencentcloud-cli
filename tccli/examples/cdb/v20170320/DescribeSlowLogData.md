**Example 1: Querying instance slow logs by search criteria**



Input: 

```
tccli cdb DescribeSlowLogData --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --StartTime 1585142640 \
    --EndTime 1585142640 \
    --UserNames usename0 \
    --DataBases database0 \
    --UserHosts userhosts0 \
    --SortBy RowsSent \
    --OrderBy DESC \
    --Limit 400 \
    --Offset 0
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

