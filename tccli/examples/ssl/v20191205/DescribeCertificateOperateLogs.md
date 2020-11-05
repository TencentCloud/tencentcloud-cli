**Example 1: Obtaining the latest 5 certificate operation logs within the latest 15 days.**



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
                "Action": "User [uin: 1234567890] applies for certificate [id: ABC1abc1]",
                "CreatedOn": "2020-01-14 15:46:38"
            },
            {
                "Action": "User [uin: 1234567890] applies for certificate [id: ABC1abc1]",
                "CreatedOn": "2020-01-14 15:45:45"
            },
            {
                "Action": "User [uin: 1234567890] applies for certificate [id: ABC1abc1]",
                "CreatedOn": "2020-01-14 14:52:19"
            },
            {
                "Action": "User [uin: 1234567890] applies for certificate [id: ABC1abc1]",
                "CreatedOn": "2020-01-14 14:50:52"
            },
            {
                "Action": "User [uin: 1234567890] applies for certificate [id: ABC1abc1]",
                "CreatedOn": "2020-01-14 14:50:21"
            }
        ],
        "RequestId": "9b397ac6-7d01-4fbc-8acc-52dd6ff0877b"
    }
}
```

