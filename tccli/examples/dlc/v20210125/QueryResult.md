**Example 1: 获取任务结果**



Input: 

```
tccli dlc QueryResult --cli-unfold-argument  \
    --NextToken tokenxxx \
    --TaskId 20210521xxxx157
```

Output: 
```
{
    "Response": {
        "TaskId": "13a636f6d****1a35f3",
        "ResultSet": "result",
        "ResultSchema": [
            {
                "Name": "Result",
                "Type": "string",
                "Comment": "success_task",
                "Precision": 0,
                "Scale": 0,
                "Nullable": "NULLABLE",
                "IsPartition": false,
                "Position": 0,
                "CreateTime": "2006-01-02 15:04:05",
                "ModifiedTime": "2006-01-02 15:04:05",
                "DataMaskStrategyInfo": null
            }
        ],
        "NextToken": "",
        "RequestId": "d5f01a69-bf51-411b-8400-0dfd25108483"
    }
}
```

