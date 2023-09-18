**Example 1: 报表嵌出创建Token接口示例-强鉴权**

报表嵌出创建Token接口示例

Input: 

```
tccli bi CreateEmbedToken --cli-unfold-argument  \
    --ExpireTime 10 \
    --Scope panel \
    --ExtraParam  \
    --ProjectId 1 \
    --UserCorpId  \
    --UserId 
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "adfacf71-c59c-4569-897d-955a1e41ee89",
        "Extra": "",
        "Data": {
            "Id": 11,
            "ProjectId": "1",
            "PageId": null,
            "ExtraParam": "",
            "Scope": "panel",
            "ExpireTime": 10,
            "CreatedUser": null,
            "CreatedAt": "2022-04-28 14:26:01",
            "UpdatedUser": null,
            "UpdatedAt": "2022-04-28 14:26:01",
            "BIToken": "300cf2a4-cfb8-47b8-9bc0-4a1f1f74bc1d",
            "UserCorpId": "",
            "UserId": ""
        }
    }
}
```

