**Example 1: 修改**



Input: 

```
tccli bi ModifyResourceUser --cli-unfold-argument  \
    --ProjectId 560 \
    --UserId u1 \
    --EntityIds 2477 \
    --ResourceType page \
    --Resource.ResourceList.0.ResourceName PageView \
    --Resource.ResourceList.0.ResourceValue True \
    --Resource.ResourceList.0.CanChange True
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "uuid",
        "Extra": "",
        "Data": null
    }
}
```

