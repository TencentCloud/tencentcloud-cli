**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeUserThirdPartyAccountInfo --cli-unfold-argument  \
    --UserName 测试用户1111 \
    --UserId userId1111
```

Output: 
```
{
    "Response": {
        "UserName": "测试用户1111",
        "UserId": "userId1111",
        "RequestId": "requestId1111",
        "ThirdPartyAccounts": [
            {
                "AccountCode": "userCode001",
                "AccountName": "第三方测试用户0001"
            }
        ]
    }
}
```

