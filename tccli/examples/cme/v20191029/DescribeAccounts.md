**Example 1: 指定手机号获取用户信息**

 

Input: 

```
tccli cme DescribeAccounts --cli-unfold-argument  \
    --Platform test \
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

**Example 2: 分布获取平台所有账号信息**

 

Input: 

```
tccli cme DescribeAccounts --cli-unfold-argument  \
    --Platform test \
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
                "UserId": "32392ca4-2c79-44f3-ad5a-63cbfa72367c",
                "Phone": "15515555056",
                "Nick": "小李",
                "Status": "Normal"
            },
            {
                "UserId": "62392ca4-2c79-44f3-ad5a-63cbfa72365d",
                "Phone": "13415555056",
                "Nick": "小张",
                "Status": "Normal"
            }
        ],
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21ad"
    }
}
```

