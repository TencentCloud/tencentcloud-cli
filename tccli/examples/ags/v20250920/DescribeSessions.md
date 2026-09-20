**Example 1: 按 Metadata 过滤 Session**

查询 Metadata 中 env 字段值为 dev 的 Session 列表。

Input: 

```
tccli ags DescribeSessions --cli-unfold-argument  \
    --SpaceId space-75f28517-9fb3-4234-9530-afa323f496bc \
    --Filters.0.Name metadata:env \
    --Filters.0.Values dev
```

Output: 
```
{
    "Response": {
        "Sessions": [
            {
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
                "Title": "modify titile",
                "UpdateTime": "2026-09-02T08:08:23Z",
                "UserId": "0001"
            }
        ],
        "TotalCount": 1,
        "RequestId": "823e1eb7-3b87-459c-a239-cfe1efafcd32"
    }
}
```

