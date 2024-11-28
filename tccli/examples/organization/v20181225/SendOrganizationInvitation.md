**Example 1: 发送企业组织邀请**



Input: 

```
tccli organization SendOrganizationInvitation --cli-unfold-argument  \
    --InviteUin 100000000001 \
    --Name "member_name" \
    --Remark '"invitation member"'
```

Output: 
```
{
    "Response": {
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214959"
    }
}
```

