**Example 1: 更新**



Input: 

```
tccli bi ModifyResourceUserGroupResource --cli-unfold-argument  \
    --ProjectId 1 \
    --UserGroupId 1 \
    --EntityIds 1 \
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
        "RequestId": "uid",
        "Extra": "",
        "Data": null
    }
}
```

