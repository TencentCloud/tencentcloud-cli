**Example 1: 创建session**



Input: 

```
tccli ags CreateSession --cli-unfold-argument  \
    --SpaceId space-75f28517-9fb3-4234-9530-afa323f496bc \
    --UserId 0001 \
    --Title 0902 test
```

Output: 
```
{
    "Response": {
        "Session": {
            "CreateTime": "2026-09-02T08:00:03Z",
            "EventCount": 0,
            "SessionId": "ffa6e867-a315-447e-917b-ba01ea557c02",
            "SpaceId": "space-75f28517-9fb3-4234-9530-afa323f496bc",
            "Title": "0902 test",
            "UpdateTime": "2026-09-02T08:00:03Z",
            "UserId": "0001"
        },
        "RequestId": "604abedd-3dfe-4d3d-a842-addbe6e28053"
    }
}
```

