**Example 1: 获取子记录的结果**

获取子记录的结果

Input: 

```
tccli wedata DescribeJobExecutionResult --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --JobId 6820260106105841034 \
    --JobExecutionId 9caaf6a0eaab11f0b434525400cb32dc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": "select 1",
            "CostTime": "15437",
            "CreateTime": "1767668323723",
            "Data": "[[\"1\"],[\"1\"]]",
            "ResultSchema": [
                {
                    "ColumnName": "1",
                    "ColumnType": "1",
                    "Comment": ""
                }
            ],
            "TotalCount": "0"
        },
        "RequestId": "fd8ce2fd-35de-47b4-a073-23e57b0c3004"
    }
}
```

