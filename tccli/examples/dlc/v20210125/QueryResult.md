**Example 1: 获取任务结果**



Input: 

```
tccli dlc QueryResult --cli-unfold-argument  \
    --NextToken xx \
    --TaskId xx
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
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

