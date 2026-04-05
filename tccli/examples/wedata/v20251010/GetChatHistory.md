**Example 1: 对话历史**



Input: 

```
tccli wedata GetChatHistory --cli-unfold-argument  \
    --WorkspaceId space1 \
    --SessionId e7451676-edf6-4c1d-b410-90fe188d2888 \
    --PageSize 1 \
    --PageNumber 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "SessionId": "e7451676-edf6-4c1d-b410-90fe188d2888"
        },
        "RequestId": "3679a9f1-6451-4a28-b874-c381c49027e8"
    }
}
```

