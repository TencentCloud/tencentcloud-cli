**Example 1: 获取任务结果**



Input: 

```
tccli dlc QueryResult --cli-unfold-argument  \
    --NextToken objectListMarker={marker}&lastReadFile={filename}&lastReadOffset \
    --TaskId 20210521195919442157
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
        "RequestId": "abc"
    }
}
```

