**Example 1: 查询**



Input: 

```
tccli cdwdoris DescribeQueryAnalyse --cli-unfold-argument  \
    --InstanceId cdwdoris-7da9fumk \
    --QueryTime 0 \
    --StartTime 2024-08-04 09:53:24 \
    --EndTime 2025-08-28 09:53:24 \
    --SQLFragment  \
    --CatalogFilter internal \
    --DatabaseFilter __internal_schema \
    --SQLTypeFilter -1 \
    --SortField Duration \
    --SortOrder ASC
```

Output: 
```
{
    "Response": {
        "QueryDetails": [
            {
                "Initiator": "str",
                "SourceAddress": "str",
                "InitialRequestId": "str",
                "Catalog": "str",
                "Database": "str",
                "SQLType": "str",
                "SQLStatement": "str",
                "StartTime": "str",
                "Duration": 1,
                "RowsRead": 1,
                "DataRead": 0,
                "MemoryUsage": 0
            }
        ],
        "TotalCount": 1,
        "CurrentPage": 1,
        "PageSize": 1,
        "TotalPages": 1,
        "RequestId": "str"
    }
}
```

