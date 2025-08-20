**Example 1: page token 清理**



Input: 

```
tccli bi ClearEmbedToken --cli-unfold-argument  \
    --ProjectId 889 \
    --UserCorpId 700000777778 \
    --Scope page \
    --PageId 8991
```

Output: 
```
{
    "Response": {
        "Extra": "Extra",
        "Msg": "Msg",
        "Data": false,
        "RequestId": "RequestId"
    }
}
```

