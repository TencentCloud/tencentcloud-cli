**Example 1: 创建企业目录配置示例**

示例是以微软 AAD 配置参考，强烈建议接口调用时，Scene填QuickStart，会自动生成一些兼容配置，Config为JSON 字符串，不同类型配置是不一致的。返回值的Id表示目录Id，非常重要，后续查询编辑都要用到此Id

Input: 

```
tccli ioa CreateCompanyDirectoryConfig --cli-unfold-argument  \
    --Type MicrosoftEntraID \
    --Name AAD配置测试 \
    --Config {"azure_tenant_id":"目录（租户）ID，必填","client_id":"应用程序(客户端) ID，必填","client_secret":"客户端密码值，必填","cloud_type":"版本类型,必填，可选值为 Global 是国际版, 21Vianet 是中国版"} \
    --SyncEnable True \
    --SyncPolicy  \
    --SyncPolicyParams  \
    --CreateAuthConfig True \
    --DisplayOnLoginPage True \
    --Scene QuickStart
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthConfigId": 121773,
            "AuthMethods": [
                "SSO认证"
            ],
            "AuthPolicyId": 39217,
            "AuthSourceId": "ioa-union-260092225bqX2szz6RRUDUxaRN5EdoA",
            "AuthSupportPlatforms": [
                "PC"
            ],
            "CreateAuthConfig": true,
            "Id": 278390,
            "IdentifySourceId": "ioa-union-260092225bqX2szz6RRUDUxaRN5EdoA",
            "Name": "AAD配置测试"
        },
        "RequestId": "a7246c21-50d0-4893-bc9e-80f24dc9e916"
    }
}
```

