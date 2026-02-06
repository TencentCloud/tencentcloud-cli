**Example 1: 添加微信公众号资产**

添加微信公众号资产

Input: 

```
tccli ctem CreateWechatOfficialAccount --cli-unfold-argument  \
    --CustomerId 100081 \
    --Name 测试 \
    --AccountId wx123 \
    --Description test
```

Output: 
```
{
    "Response": {
        "Id": 12,
        "RequestId": "4f8849b5-3feb-4894-97bc-41c6d4bbef31"
    }
}
```

