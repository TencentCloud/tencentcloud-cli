**Example 1: 创建 API Key**



Input: 

```
tccli dlc CreateApiKey --cli-unfold-argument  \
    --Name chenfan_test
```

Output: 
```
{
    "Response": {
        "ApiKey": "sk-*****************************************************",
        "ApiKeyId": "apikey-20260615204858-736d",
        "AppId": 200000000,
        "CreateTime": 1781527738362,
        "Name": "chenfan_test",
        "Status": "Revoked",
        "SubAccountUin": "7***********",
        "Uin": "7***********",
        "UpdateTime": 1781527738362,
        "RequestId": "f55e63df-8774-4e56-8c79-bbfaa60b57d7"
    }
}
```

