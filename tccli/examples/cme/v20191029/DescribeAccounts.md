**Example 1: 获取用户信息**



Input: 

```
tccli cme DescribeAccounts --cli-unfold-argument  \
    --Platform 100001 \
    --Phone 15517177077 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccountInfoSet": [
            {
                "UserId": "72392ca4-2c79-44f3-ad5a-63cbfa72367c",
                "Phone": "15515555055",
                "Nick": "Nick",
                "Status": "Normal"
            }
        ],
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

