**Example 1: 对话列表**



Input: 

```
tccli wedata ListChats --cli-unfold-argument  \
    --WorkspaceId space1 \
    --PageSize 1 \
    --PageNumber 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreatedAt": "1764831674360",
                    "SessionId": "62246040-fb06-4b40-9c13-a65c5a367df7",
                    "Title": "",
                    "UpdatedAt": "1764831674360"
                },
                {
                    "CreatedAt": "1764761138992",
                    "SessionId": "663f1de0-8d58-4597-a94b-922ccf87af97",
                    "Title": "",
                    "UpdatedAt": "1764761138992"
                },
                {
                    "CreatedAt": "1764762648484",
                    "SessionId": "e7451676-edf6-4c1d-b410-90fe188d2888",
                    "Title": "",
                    "UpdatedAt": "1764762678025"
                },
                {
                    "CreatedAt": "1764831579894",
                    "SessionId": "1bdf868f-978d-4be6-988c-53fa0df51973",
                    "Title": "",
                    "UpdatedAt": "1764831579894"
                }
            ],
            "TotalCount": 4
        },
        "RequestId": "733dd36e-6248-493a-a2e9-f43e535bf528"
    }
}
```

