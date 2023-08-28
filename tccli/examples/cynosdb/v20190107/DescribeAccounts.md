**Example 1: 查询数据库账号列表**

查询数据库账号列表

Input: 

```
tccli cynosdb DescribeAccounts --cli-unfold-argument  \
    --ClusterId cynosdbysql-on5xw0ni
```

Output: 
```
{
    "Response": {
        "AccountSet": [
            {
                "AccountName": "abc",
                "Description": "abc",
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00",
                "Host": "abc",
                "MaxUserConnections": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

