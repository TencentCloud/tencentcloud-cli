**Example 1: 创建组织成员**



Input: 

```
tccli organization CreateOrganizationMember --cli-unfold-argument  \
    --Remark create member \
    --Name member_name \
    --NodeId 1001 \
    --AccountName member_name \
    --PermissionIds 1 2 \
    --PolicyType Finical \
    --IdentityRoleID 1
```

Output: 
```
{
    "Response": {
        "Uin": 111111111111,
        "RequestId": "1a556fac-cd38-4732-86ef-6283d6abddd7"
    }
}
```

