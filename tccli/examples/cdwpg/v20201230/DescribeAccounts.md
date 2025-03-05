**Example 1: 账号管理**



Input: 

```
tccli cdwpg DescribeAccounts --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --InstanceId cdwpg_xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Accounts": [
            {
                "InstanceId": "cdwpg_xx",
                "UserName": "cran",
                "Perms": [
                    "sds"
                ]
            }
        ],
        "RequestId": "xxdsds"
    }
}
```

