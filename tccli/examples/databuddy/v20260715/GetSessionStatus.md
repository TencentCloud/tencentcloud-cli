**Example 1: GetSessionStatus**

GetSessionStatus

Input: 

```
tccli databuddy GetSessionStatus --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --Items.0.RuntimeId 2074423297173803008 \
    --Items.0.SessionId 2074423297173803008
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "RuntimeId": "2074423297173803008",
                    "SessionId": "2074423297173803008",
                    "TaskStatus": "completed"
                }
            ]
        },
        "RequestId": "691774a7-9463-4e57-904c-d49f54bd99e2"
    }
}
```

