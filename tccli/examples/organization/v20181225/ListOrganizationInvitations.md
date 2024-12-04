**Example 1: 获取邀请信息列表**



Input: 

```
tccli organization ListOrganizationInvitations --cli-unfold-argument  \
    --Invited 101 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Invitations": [
            {
                "Id": 1,
                "Uin": 1000001,
                "HostUin": 1000001,
                "HostName": "host_name",
                "HostMail": "23**@qq.com",
                "Status": 1,
                "Name": "member_name",
                "Remark": "invitation member",
                "OrgType": 1,
                "InviteTime": "2021-03-04 12:22:21",
                "ExpireTime": "2021-03-04 12:22:21"
            }
        ],
        "RequestId": "97fd9345-cfd6-4b93-8205-e25d21ecd26e"
    }
}
```

