**Example 1: 获取实例postgres-apzvwncr的用户列表**

获取实例postgres-apzvwncr的用户列表

Input: 

```
tccli postgres DescribeAccounts --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "Details": [
            {
                "UserName": "root",
                "Status": 2,
                "Remark": "（测试）这个账户是无效的",
                "DBInstanceId": "postgres-apzvwncr",
                "UpdateTime": "2018-06-12 17:21:57",
                "CreateTime": "2018-06-12 17:21:54"
            }
        ]
    }
}
```

