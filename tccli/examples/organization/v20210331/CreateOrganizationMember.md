**Example 1: 创建组织成员**



Input: 

```
tccli organization CreateOrganizationMember --cli-unfold-argument  \
    --Name member_name \
    --PolicyType Financial \
    --PermissionIds 1 2 \
    --NodeId 100000000001 \
    --AccountName member_name
```

Output: 
```
{
    "Response": {
        "Uin": 111111111111,
        "RequestId": "baf86769-f4d5-47bd-8efc-3644add42458"
    }
}
```

