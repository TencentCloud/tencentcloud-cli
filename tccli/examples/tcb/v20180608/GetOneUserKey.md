**Example 1: 用户获取密钥对详情**



Input: 

```
tccli tcb GetOneUserKey --cli-unfold-argument  \
    --EnvId tcb-paas-e2e-main-vfc3g64mbqt7 \
    --KeyID create_key_2
```

Output: 
```
{
    "Response": {
        "RequestId": "0b403204-36c4-11f0-857c-fa6cef78999d",
        "UserKeyInfo": {
            "AuthTypeCode": "PublicAccountOpenService",
            "AuthTypeName": "公众号开放能力",
            "BindServiceList": {
                "Apis": [],
                "Mcp": []
            },
            "Description": "",
            "Ext": "{\"appId\":\"wx2fc2dd428840ae3d\",\"appsecret\":\"\"}",
            "KeyID": "create_key_2",
            "Name": "更新密钥对",
            "Status": "已发布"
        }
    }
}
```

