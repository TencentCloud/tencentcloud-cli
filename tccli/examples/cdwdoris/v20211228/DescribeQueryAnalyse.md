**Example 1: 查询**



Input: 

```
tccli cdwdoris DescribeQueryAnalyse --cli-unfold-argument  \
    --InstanceId abc \
    --UserName abc \
    --PassWord abc \
    --StartTime abc \
    --EndTime abc \
    --SQLFragment abc \
    --CatalogFilter abc \
    --DatabaseFilter abc \
    --SQLTypeFilter abc \
    --SortField abc \
    --SortOrder abc
```

Output: 
```
{
    "Response": {
        "QueryDetails": [
            {
                "Initiator": "abc",
                "SourceAddress": "abc",
                "InitialRequestId": "abc",
                "Catalog": "abc",
                "Database": "abc",
                "SQLType": "abc",
                "SQLStatement": "abc",
                "StartTime": "abc",
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
        "RequestId": "abc"
    }
}
```

