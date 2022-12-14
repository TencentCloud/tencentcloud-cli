**Example 1: 查询数据库管理账号**



Input: 

```
tccli cynosdb DescribeAccounts --cli-unfold-argument  \
    --ClusterId cynosdbysql-on5xw0ni
```

Output: 
```
{
    "Response": {
        "RequestId": "150918",
        "TotalCount": 1,
        "AccountSet": [
            {
                "UpdateTime": "2018-06-28 23:28:52",
                "Host": "xx",
                "CreateTime": "2018-06-28 23:28:52",
                "Description": "默认用户asdf",
                "MaxUserConnections": 0,
                "AccountName": "admin"
            }
        ]
    }
}
```

