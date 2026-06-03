**Example 1: 更新**



Input: 

```
tccli bi ModifyResourceUserGroup --cli-unfold-argument  \
    --ProjectId 1 \
    --UserGroupIds 108 \
    --ResourceType page \
    --QueryChildren False \
    --Resource.EntityId 1 \
    --Resource.NodeType 2 \
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

