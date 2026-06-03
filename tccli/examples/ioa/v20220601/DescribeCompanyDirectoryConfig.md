**Example 1: 获取企业目录配置详情**

Config为目录生成后的完整配置，敏感字段会被直接脱敏返回

Input: 

```
tccli ioa DescribeCompanyDirectoryConfig --cli-unfold-argument  \
    --Id 278390
```

Output: 
```
{
    "Response": {
        "Data": {
            "Config": "{\"attribute_map\":{\"avatar\":\"-\",\"email\":\"mail\",\"extended_id\":\"-\",\"name\":\"displayName\",\"phone\":\"mobilePhone\",\"user_id\":\"userPrincipalName\"},\"azure_tenant_id\":\"目录（租户）ID，必填\",\"client_id\":\"应用程序(客户端) ID，必填\",\"client_secret\":\"******\",\"cloud_type\":\"版本类型,必填，可选值为 Global 是国际版, 21Vianet 是中国版\",\"extended_attributes\":[],\"group_ids\":\"\",\"sensitive_fields\":[\"client_secret\"],\"status_attribute\":{\"type\":\"none\"}}",
            "CreateAuthConfig": true,
            "Description": "",
            "DisplayOnLoginPage": true,
            "Id": 278390,
            "Name": "AAD配置测试",
            "SourceId": "ioa-union-260092225bqX2szz6RRUDUxaRN5EdoA",
            "SyncEnable": true,
            "SyncPolicy": "4hours",
            "SyncPolicyParams": "{\"week\":\"SAT\",\"hour\":\"02\",\"minute\":\"30\"}",
            "Type": "MicrosoftEntraID"
        },
        "RequestId": "ed8ce64f-ecd5-46b4-a47c-9bdc394e3db3"
    }
}
```

