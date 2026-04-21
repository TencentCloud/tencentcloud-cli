**Example 1: ModifyUserGroup**

ModifyUserGroup

Input: 

```
tccli bi ModifyUserGroup --cli-unfold-argument  \
    --UpdateList.0.AdminUserId 700000280185 \
    --UpdateList.0.Description 123 \
    --UpdateList.0.GroupName 测试用户组 \
    --UpdateList.0.Location 0 \
    --UpdateList.0.ParentId -1 \
    --UpdateList.0.Id 273
```

Output: 
```
{
    "Response": {
        "RequestId": "fae2a374-801a-49df-8544-8fd865d4d34a"
    }
}
```

