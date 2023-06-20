**Example 1: 创建公共配置项**

创建公共配置项

Input: 

```
tccli tsf CreatePublicConfigWithDetailResp --cli-unfold-argument  \
    --ConfigName abc \
    --ConfigVersion abc \
    --ConfigVersionDesc abc \
    --ConfigValue abc \
    --ConfigType abc \
    --EncodeWithBase64 True \
    --ProgramIdList abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "ConfigId": "abc",
            "ConfigName": "abc",
            "ConfigVersion": "abc",
            "ConfigVersionDesc": "abc",
            "ConfigValue": "abc",
            "ConfigType": "abc",
            "CreationTime": "abc",
            "ApplicationId": "abc",
            "ApplicationName": "abc",
            "DeleteFlag": true,
            "LastUpdateTime": "abc",
            "ConfigVersionCount": 0
        },
        "RequestId": "abc"
    }
}
```

