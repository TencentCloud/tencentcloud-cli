**Example 1: 请求示例**



Input: 

```
tccli eiam ListUsersInOrgNode --cli-unfold-argument  \
    --OrgNodeId 7999987a-c9dc-4dd2-b3e2-b52f53317aa6 \
    --IncludeOrgNodeChildInfo true
```

Output: 
```
{
    "Response": {
        "RequestId": "5bac190a-e341-4dd2-a061-c4034a299e86",
        "OrgNodeChildUserInfo": [
            {
                "OrgNodeId": "cd86d39c-07d4-443c-b7a2-82117338957c",
                "UserInfo": [],
                "TotalUserNum": 0
            }
        ],
        "OrgNodeId": "7999987a-c9dc-4dd2-b3e2-b52f53317aa6",
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
                "UserId": "2877f61b-3467-46f4-a6cb-eebd3cce660a",
                "DisplayName": "接口创建用户"
            }
        ],
        "TotalUserNum": 3
    }
}
```

