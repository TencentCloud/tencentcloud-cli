**Example 1: 查询数据库列表**



Input: 

```
tccli cynosdb DescribeClusterDetailDatabases --cli-unfold-argument  \
    --ClusterId cynosdbpg-xxxxxxx \
    --Limit 20 \
    --DbName test \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DbInfos": [
            {
                "Status": "running",
                "UserHostPrivileges": [],
                "UpdateTime": "0001-01-01T00:00:00Z",
                "Description": "",
                "DbId": 0,
                "CharacterSet": "",
                "ClusterId": "",
                "DbName": "mysql",
                "Uin": "",
                "AppId": 0,
                "CollateRule": "",
                "CreateTime": "0001-01-01T00:00:00Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6e094b68-0a37-11ec-97e7-525400542aa6"
    }
}
```

