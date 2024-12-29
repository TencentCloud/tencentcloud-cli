**Example 1: 创建配置模板**

创建配置模板

Input: 

```
tccli tsf CreateConfigTemplateWithDetailResp --cli-unfold-argument  \
    --ConfigTemplateName config_temp \
    --ConfigTemplateDesc This is desc \
    --ConfigTemplateType Ribbon \
    --ConfigTemplateValue #请求处理超时时间\\nribbon.ReadTimeout: 5000\\n#请求连接超时时间\\nribbon.ConnectTimeout: 2000\\n#同一实例最大重试次数，不包括首次调用\\nribbon.MaxAutoRetries: 0\\n#重试其他实例的最大重试次数，不包括首次所选的server\\nribbon.MaxAutoRetriesNextServer: 1\\n#是否对所有操作请求都进行重试\\nribbon.OkToRetryOnAllOperations: false\\n \
    --ProgramIdList program-6a79x94v
```

Output: 
```
{
    "Response": {
        "RequestId": "6d940d10-9545-4481-bbc2-eb0d6016f069",
        "Result": {
            "ConfigTemplateDesc": "This is desc",
            "ConfigTemplateId": "dcfg_temp-ymw5o65v",
            "ConfigTemplateName": "config_temp",
            "ConfigTemplateType": "Ribbon",
            "ConfigTemplateValue": "#请求处理超时时间\\\\nribbon.ReadTimeout: 5000\\\\n#请求连接超时时间\\\\nribbon.ConnectTimeout: 2000\\\\n#同一实例最大重试次数，不包括首次调用\\\\nribbon.MaxAutoRetries: 0\\\\n#重试其他实例的最大重试次数，不包括首次所选的server\\\\nribbon.MaxAutoRetriesNextServer: 1\\\\n#是否对所有操作请求都进行重试\\\\nribbon.OkToRetryOnAllOperations: false\\\\n",
            "CreateTime": null,
            "UpdateTime": null
        }
    }
}
```

