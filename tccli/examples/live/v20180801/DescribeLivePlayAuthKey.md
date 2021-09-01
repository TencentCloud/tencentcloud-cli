**Example 1: 请求示例**



Input: 

```
tccli live DescribeLivePlayAuthKey --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com
```

Output: 
```
{
    "Response": {
        "PlayAuthKeyInfo": {
            "DomainName": "5000.livepush.myqcloud.com",
            "Enable": 1,
            "AuthKey": "xxxx",
            "AuthDelta": 300,
            "AuthBackKey": "xxx"
        },
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

