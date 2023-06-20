**Example 1: 创建文件配置项**

为应用创建文件配置

Input: 

```
tccli tsf CreateFileConfigWithDetailResp --cli-unfold-argument  \
    --ConfigName abc \
    --ConfigVersion abc \
    --ConfigVersionDesc abc \
    --ConfigFileName abc \
    --ConfigFileValue abc \
    --ConfigFileCode abc \
    --ApplicationId abc \
    --ConfigFilePath abc \
    --ConfigPostCmd abc \
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
            "ConfigFileName": "abc",
            "ConfigFileValue": "abc",
            "ConfigFileCode": "abc",
            "CreationTime": "abc",
            "ApplicationId": "abc",
            "ApplicationName": "abc",
            "DeleteFlag": true,
            "ConfigVersionCount": 0,
            "LastUpdateTime": "abc",
            "ConfigFilePath": "abc",
            "ConfigPostCmd": "abc",
            "ConfigFileValueLength": 1
        },
        "RequestId": "abc"
    }
}
```

