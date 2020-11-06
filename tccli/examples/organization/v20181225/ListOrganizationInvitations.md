**Example 1: 获取邀请信息列表**



Input: 

```
tccli organization ListOrganizationInvitations --cli-unfold-argument  \
    --Invited 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Invitations": [
            {
                "Id": 1,
                "Uin": 1,
                "HostUin": 1,
                "HostName": "aa",
                "HostMail": "aa@qq.com",
                "Status": 1,
                "Name": "aa",
                "Remark": "",
                "OrgType": 1,
                "InviteTime": "2019-10-10 00:00:00",
                "ExpireTime": "2019-10-10 00:00:00"
            }
        ],
        "RequestId": "97fd9345-cfd6-4b93-8205-e25d21ecd26e"
    }
}
```

