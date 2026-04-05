**Example 1: demo**



Input: 

```
tccli wedata ValidateFileName --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --ParentMeta.FileId 791609522159632384 \
    --NewName Users
```

Output: 
```
{
    "Response": {
        "Data": {
            "Exists": true
        },
        "RequestId": "0777f75a-e61a-4019-a40f-45d36659041c"
    }
}
```

