**Example 1: 删除USG**



Input: 

```
tccli vpc DeleteUSGInternal --cli-unfold-argument  \
    --DeleteUSGRequest.0.UsgId 123123 \
    --DeleteUSGRequest.0.ProjectId 123
```

Output: 
```
{
    "Response": {
        "DeleteUSGResult": [
            {
                "UsgId": "sg-an7f7qxx",
                "ErrorCode": 0,
                "ErrorInfo": "success"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

