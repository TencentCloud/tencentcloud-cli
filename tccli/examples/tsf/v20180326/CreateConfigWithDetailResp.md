**Example 1: 创建配置项**

为应用创建配置项

Input: 

```
tccli tsf CreateConfigWithDetailResp --cli-unfold-argument  \
    --ConfigName abc \
    --ConfigVersion abc \
    --ConfigVersionDesc abc \
    --ConfigValue abc \
    --ApplicationId abc \
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

