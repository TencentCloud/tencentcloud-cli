**Example 1: 查询用户列表**



Input: 

```
tccli tcb DescribeUserList --cli-unfold-argument  \
    --EnvId test_envId \
    --PageNo 1 \
    --PageSize 10 \
    --Name zhang \
    --NickName 张 \
    --Phone 13900139000 \
    --Email zhangsan@example.com
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 100,
            "UserList": [
                {
                    "AvatarUrl": "https://example.com/avatars/zhangsan.jpg",
                    "Description": "研发部门技术总监",
                    "Email": "zhangsan@example.com",
                    "Name": "zhangsan",
                    "NickName": "张三",
                    "Phone": "13800138000",
                    "Type": "internalUser",
                    "Uid": "1001",
                    "UserStatus": "ACTIVE"
                }
            ]
        },
        "RequestId": "eb985f06-ebb2-4d1f-a224-2f5bdc0c4eb4"
    }
}
```

