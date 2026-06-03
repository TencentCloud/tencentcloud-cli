**Example 1: 更新目录配置示例**

先通过DescribeCompanyDirectoryConfig 获取配置数据后，在修改数据调用此接口请求变更

Input: 

```
tccli ioa ModifyCompanyDirectoryConfig --cli-unfold-argument  \
    --Type MicrosoftEntraID \
    --Name AAD配置测试2 \
    --Config {"attribute_map":{"avatar":"-","email":"mail","extended_id":"-","name":"displayName","phone":"mobilePhone","user_id":"userPrincipalName"},"azure_tenant_id":"目录（租户）ID，必填","client_id":"应用程序(客户端) ID，必填","client_secret":"******","cloud_type":"版本类型,必填，可选值为 Global 是国际版, 21Vianet 是中国版","extended_attributes":[],"group_ids":"","sensitive_fields":["client_secret"],"status_attribute":{"type":"none"}} \
    --SyncEnable True \
    --SyncPolicy 4hours \
    --SyncPolicyParams {"week":"SAT","hour":"02","minute":"30"} \
    --CreateAuthConfig True \
    --DisplayOnLoginPage True \
    --Id 278390
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthConfigId": 0,
            "AuthMethods": [],
            "AuthPolicyId": 0,
            "AuthSourceId": "",
            "AuthSupportPlatforms": [],
            "CreateAuthConfig": true,
            "Id": 278390,
            "IdentifySourceId": "ioa-union-260092225bqX2szz6RRUDUxaRN5EdoA",
            "Name": "AAD配置测试2"
        },
        "RequestId": "91d4f838-654f-4f6e-b265-b012b81b4614"
    }
}
```

