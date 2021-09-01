**Example 1: 获取用户近15天前5条证书操作日志**



Input: 

```
tccli ssl DescribeCertificateOperateLogs --cli-unfold-argument  \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "AllTotal": 31,
        "TotalCount": 5,
        "OperateLogs": [
            {
                "Action": "用户[uin: 1234567890] 申请 证书[id: ABC1abc1]",
                "CreatedOn": "2020-01-14 15:46:38"
            },
            {
                "Action": "用户[uin: 1234567890] 申请 证书[id: ABC1abc1]",
                "CreatedOn": "2020-01-14 15:45:45"
            },
            {
                "Action": "用户[uin: 1234567890] 申请 证书[id: ABC1abc1]",
                "CreatedOn": "2020-01-14 14:52:19"
            },
            {
                "Action": "用户[uin: 1234567890] 申请 证书[id: ABC1abc1]",
                "CreatedOn": "2020-01-14 14:50:52"
            },
            {
                "Action": "用户[uin: 1234567890] 申请 证书[id: ABC1abc1]",
                "CreatedOn": "2020-01-14 14:50:21"
            }
        ],
        "RequestId": "9b397ac6-7d01-4fbc-8acc-52dd6ff0877b"
    }
}
```

