**Example 1: Sending an invitation to join an organization**



Input: 

```
tccli organization SendOrganizationInvitation --cli-unfold-argument  \
    --InviteUin 123\
    --Name "test"\
    --Remark "test"
```

Output: 
```
{
    "Response": {
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

