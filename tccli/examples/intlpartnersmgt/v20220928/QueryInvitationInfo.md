**Example 1: 查询邀请链接使用信息**



Input: 

```
tccli intlpartnersmgt QueryInvitationInfo --cli-unfold-argument  \
    --InvitationToken 17772490a7664fc1f3fd31******63d8
```

Output: 
```
{
    "Response": {
        "RequestId": "9876218d-3faf-4a7f-ad41-5aba65b80d35",
        "InvitationInfo": [
            {
                "InvitationToken": "17772490a7664fc1f3fd31******63d8",
                "CreateTime": "2025-03-28 06:49:30",
                "Status": 2,
                "UseTime": "2025-03-25 14:50:14",
                "ClientUin": 800001808094,
                "ClientMail": "1**********8@gmail.com",
                "ClientType": 2,
                "BindTime": "2025-03-25 14:51:04"
            }
        ]
    }
}
```

