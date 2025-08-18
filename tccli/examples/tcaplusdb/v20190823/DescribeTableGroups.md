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
                "TableGroupId": "18322",
                "TableGroupName": "groupname",
                "CreatedTime": "2020-09-22 00:00:00",
                "TableCount": 1,
                "TotalSize": 1,
                "TxhBackupExpireDay": 1,
                "EnableMysql": 1,
                "MysqlConnIp": "192.1.2.3",
                "MysqlConnPort": 13722
            }
        ],
        "RequestId": "13232-13523"
    }
}
```

