**Example 1: 请求示例**



Input: 

```
tccli eiam ListUsersInUserGroup --cli-unfold-argument  \
    --UserGroupId 1453013c-d0e9-424b-b9c7-dabcea3bd0ca
```

Output: 
```
{
    "Response": {
        "TotalNum": 3,
        "RequestId": "cbceae17-3098-4ac1-813f-8db40ee01e05",
        "UserGroupId": "1453013c-d0e9-424b-b9c7-dabcea3bd0ca",
        "UserInfo": [
            {
                "UserId": "5c1ab60e-4844-4d92-8708-82257657d916",
                "DisplayName": "接口创建用户"
            },
            {
                "UserId": "df68819a-804b-44f8-af68-682b28d5c02e",
                "DisplayName": "接口创建用户"
            },
            {
                "UserId": "3945dcb0-e433-4fd0-a69b-b5074abe3cbd",
                "DisplayName": "修改用户"
            }
        ]
    }
}
```

