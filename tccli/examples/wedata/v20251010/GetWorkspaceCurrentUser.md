**Example 1: 获取工作空间当前用户**



Input: 

```
tccli wedata GetWorkspaceCurrentUser --cli-unfold-argument  \
    --WorkspaceId 1769*******842890
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "130*****87",
            "OwnerUin": "6****0****78",
            "PolicyInfo": [],
            "UserInfo": {
                "Nickname": "we**t*3*-***********.com",
                "Uin": "70***2****18",
                "UserName": "we***a*0*de*******n*.com",
                "UserTag": ""
            }
        },
        "RequestId": "76811b12-a0cc-4549-81a1-cbcbebf5f401"
    }
}
```

