**Example 1: 账号管理**



Input: 

```
tccli cdwpg DescribeAccounts --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --InstanceId cdwpg_rzshdeh1
```

Output: 
```
{
    "Response": {
        "Accounts": [
            {
                "InstanceId": "cdwpg-rzshdeh1",
                "Perms": [
                    "Create role",
                    "Create DB"
                ],
                "UserName": "dbadmin"
            }
        ],
        "RequestId": "88aeb3ac-19d8-4c89-b4e2-905cbf74100d",
        "ErrorMsg": "",
        "TotalCount": 1
    }
}
```

