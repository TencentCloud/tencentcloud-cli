**Example 1: 邀请成员**

邀请成员

Input: 

```
tccli organization InviteOrganizationMember --cli-unfold-argument  \
    --Remark invitation member \
    --MemberUin 111111111111 \
    --Name member_name \
    --NodeId 1001 \
    --PermissionIds 1 2 \
    --PolicyType Financial \
    --PayUin 100000000001
```

Output: 
```
{
    "Response": {
        "RequestId": "9be34d82-b614-4010-8cd8-d907b4d303f2"
    }
}
```

