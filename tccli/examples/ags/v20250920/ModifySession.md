**Example 1: 修改会话的元数据**



Input: 

```
tccli ags ModifySession --cli-unfold-argument  \
    --SpaceId space-75f28517-9fb3-4234-9530-afa323f496bc \
    --UserId 0001 \
    --SessionId ffa6e867-a315-447e-917b-ba01ea557c02 \
    --Metadata.0.Name env \
    --Metadata.0.Value dev
```

Output: 
```
{
    "Response": {
        "Session": {
            "CreateTime": "2026-09-02T08:00:03Z",
            "EventCount": 0,
            "Metadata": [
                {
                    "Name": "env",
                    "Value": "dev"
                }
            ],
            "SessionId": "ffa6e867-a315-447e-917b-ba01ea557c02",
            "SpaceId": "space-75f28517-9fb3-4234-9530-afa323f496bc",
            "Title": "0902 test",
            "UpdateTime": "2026-09-02T08:06:45Z",
            "UserId": "0001"
        },
        "RequestId": "4c41c3b7-6c43-4dde-ade3-b460400933bb"
    }
}
```

