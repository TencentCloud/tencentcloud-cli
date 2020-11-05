**Example 1: Getting user list for instance postgres-apzvwncr**



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
                "Remark": "(Test) this account is invalid",
                "DBInstanceId": "postgres-apzvwncr",
                "UpdateTime": "2018-06-12 17:21:57",
                "CreateTime": "2018-06-12 17:21:54"
            }
        ]
    }
}
```

