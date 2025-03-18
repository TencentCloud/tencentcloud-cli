**Example 1: 获取statement运行结果**

本接口用于获取statement运行结果。

Input: 

```
tccli dlc DescribeNotebookSessionStatementSqlResult --cli-unfold-argument  \
    --TaskId 20210521195919442157 \
    --MaxResults 100 \
    --NextToken objectListMarker={marker}&lastReadFile={filename}&lastReadOffset
```

Output: 
```
{
    "Response": {
        "TaskId": "0be002bf-4233-430c-abed-f99b6e375513",
        "ResultSet": "SqlResult",
        "ResultSchema": [
            {
                "Name": "title",
                "Type": "string",
                "Comment": "sql test",
                "Precision": 0,
                "Scale": 0,
                "Nullable": "NULLABLE",
                "Position": 0,
                "CreateTime": "",
                "ModifiedTime": "",
                "IsPartition": true
            }
        ],
        "NextToken": "nexttokenxxx",
        "OutputPath": "lakefs://*/*/.system/result/20250109/*/",
        "RequestId": "dd329ee3-ec32-4249-a7aa-596f3d47d703",
        "UseTime": 10,
        "AffectRows": 10
    }
}
```

