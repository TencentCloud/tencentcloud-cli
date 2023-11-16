**Example 1: 查询数据表名称列表**



Input: 

```
tccli dlc DescribeTablesName --cli-unfold-argument  \
    --Limit 0 \
    --Offset 1 \
    --DatabaseName abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --DatasourceConnectionName abc \
    --StartTime abc \
    --EndTime abc \
    --Sort abc \
    --Asc True \
    --TableType abc \
    --TableFormat abc
```

Output: 
```
{
    "Response": {
        "TableNameList": [
            "abc"
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

