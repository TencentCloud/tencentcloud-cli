**Example 1: 创建组织成员**



Input: 

```
tccli organization CreateOrganizationMember --cli-unfold-argument  \
    --Remark test \
    --Name test \
    --NodeId 27 \
    --AccountName test \
    --PermissionIds 1 2 \
    --PolicyType Finical \
    --PayUin  \
    --IdentityRoleID 1
```

Output: 
```
{
    "Response": {
        "Uin": 100001919,
        "RequestId": "1a556fac-cd38-4732-86ef-6283d6abddd7"
    }
}
```

