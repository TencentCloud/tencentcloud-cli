**Example 1: 查询表格组列表**

查询表格组列表

Input: 

```
tccli tcaplusdb DescribeTableGroups --cli-unfold-argument  \
    --ClusterId 6179109757
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "TableGroups": [
            {
                "TableGroupId": "abc",
                "TableGroupName": "abc",
                "CreatedTime": "2020-09-22 00:00:00",
                "TableCount": 1,
                "TotalSize": 1,
                "TxhBackupExpireDay": 1,
                "EnableMysql": 1,
                "MysqlConnIp": "abc",
                "MysqlConnPort": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

