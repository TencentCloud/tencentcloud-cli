**Example 1: 创建配置模板**

创建配置模板

Input: 

```
tccli tsf CreateConfigTemplateWithDetailResp --cli-unfold-argument  \
    --ConfigTemplateName abc \
    --ConfigTemplateDesc abc \
    --ConfigTemplateType abc \
    --ConfigTemplateValue abc \
    --ProgramIdList abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "ConfigTemplateId": "abc",
            "ConfigTemplateName": "abc",
            "ConfigTemplateDesc": "abc",
            "ConfigTemplateType": "abc",
            "ConfigTemplateValue": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc"
        },
        "RequestId": "xxxxxxxxxxx"
    }
}
```

