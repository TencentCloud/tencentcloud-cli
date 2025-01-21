**Example 1: 查询数据表名称列表**



Input: 

```
tccli dlc DescribeTablesName --cli-unfold-argument  \
    --DatabaseName dlc_db \
    --Limit 20 \
    --Offset 0 \
    --Filters.0.Name table-name \
    --Filters.0.Values dlc_detail \
    --DatasourceConnectionName emr_hive \
    --StartTime 2024-12-02 15:04:05 \
    --EndTime 2025-01-02 15:04:05 \
    --Sort UpdateTime \
    --Asc True \
    --TableType Table \
    --TableFormat HIVE
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-102073fb4fe8",
        "TableNameList": [
            "dlc_detail"
        ],
        "TotalCount": 1
    }
}
```

