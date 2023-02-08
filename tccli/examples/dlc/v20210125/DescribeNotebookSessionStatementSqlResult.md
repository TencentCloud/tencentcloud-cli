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
        "ResultSchema": [
            {
                "Comment": "xx",
                "Scale": 0,
                "Name": "xx",
                "Nullable": "xx",
                "Precision": 0,
                "Type": "xx"
            }
        ],
        "NextToken": "xx",
        "ResultSet": "xx",
        "OutputPath": "cosn:xx",
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

