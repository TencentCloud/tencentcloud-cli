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
        "TaskId": "abc",
        "ResultSet": "abc",
        "ResultSchema": [
            {
                "Name": "abc",
                "Type": "abc",
                "Comment": "abc",
                "Precision": 0,
                "Scale": 0,
                "Nullable": "abc",
                "Position": 0,
                "CreateTime": "abc",
                "ModifiedTime": "abc",
                "IsPartition": true
            }
        ],
        "NextToken": "abc",
        "OutputPath": "abc",
        "RequestId": "abc"
    }
}
```

