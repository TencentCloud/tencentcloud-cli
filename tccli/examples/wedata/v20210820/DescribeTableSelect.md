**Example 1: 查询表的select语句**



Input: 

```
tccli wedata DescribeTableSelect --cli-unfold-argument  \
    --TableId guid_of_table_***
```

Output: 
```
{
    "Response": {
        "RequestId": "req_id_***",
        "Select": "SELECT `col1`, `col2`, `col3`, `pt_day` FROM `database_name`.`table_name` WHERE `pt_day` = '${bizdate}' LIMIT 1000"
    }
}
```

