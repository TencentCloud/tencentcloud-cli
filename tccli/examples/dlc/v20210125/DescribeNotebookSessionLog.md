**Example 1: 查询交互式 session日志**

查询交互式 session日志

Input: 

```
tccli dlc DescribeNotebookSessionLog --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742 \
    --Limit 200 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Logs": [
            "log"
        ],
        "Limit": 200,
        "Offset": 0,
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

