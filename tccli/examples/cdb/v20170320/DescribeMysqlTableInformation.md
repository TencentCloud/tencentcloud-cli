**Example 1: 查询数据库表信息**



Input: 

```
tccli cdb DescribeMysqlTableInformation --cli-unfold-argument  \
    --AppIdUser 251051041 \
    --Operator op_user \
    --InstanceId cdb-0mu6taqx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "DBName": "wy_test_1",
                "TableFields": [
                    {
                        "Field": "id",
                        "Type": "int(11)"
                    },
                    {
                        "Field": "k",
                        "Type": "varchar(1000)"
                    },
                    {
                        "Field": "v",
                        "Type": "varchar(10240)"
                    }
                ],
                "TableName": "whitelist_kv",
                "UpdateTime": "2024-01-04 12:10:13"
            }
        ],
        "TotalCount": 1,
        "RequestId": "cafebabe-bf9cc173-222e031e-dddd"
    }
}
```

