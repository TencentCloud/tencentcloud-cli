**Example 1: 创建成员**



Input: 

```
tccli organization CreateOrganizationMember --cli-unfold-argument  \
    --Remark test \
    --Name test \
    --NodeId 27 \
    --AccountName test \
    --PermissionIds 1 \
    --PolicyType Finical
```

Output: 
```
{
    "Response": {
        "RequestId": "1a556fac-cd38-4732-86ef-6283d6abddd7"
    }
}
```

