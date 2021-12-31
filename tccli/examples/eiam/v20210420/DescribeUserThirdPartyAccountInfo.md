**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeUserThirdPartyAccountInfo --cli-unfold-argument  \
    --UserName xx \
    --UserId xx
```

Output: 
```
{
    "Response": {
        "UserName": "xx",
        "UserId": "xx",
        "RequestId": "xx",
        "ThirdPartyAccounts": [
            {
                "AccountCode": "xx",
                "AccountName": "xx"
            }
        ]
    }
}
```

