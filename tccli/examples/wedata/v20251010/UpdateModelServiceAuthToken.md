**Example 1: UpdateModelServiceAuthToken**



Input: 

```
tccli wedata UpdateModelServiceAuthToken --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --ServiceGroupId 960ed2fc-f40e-4b34-b662-a3ed689e035b \
    --AuthToken.Base.Name test021 \
    --AuthToken.Base.Description aaaa \
    --AuthToken.Base.Value 1f70c8590d3b5e7
```

Output: 
```
{
    "Response": {
        "Data": {
            "TiOneRequestId": "904a4595-24fd-4f9f-8e55-e4a81af394b8"
        },
        "RequestId": "e244e125-5f21-481e-aaf0-946631a12bb0"
    }
}
```

