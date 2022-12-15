**Example 1: 创建参数模板示例**

数据库版本为14，引擎为postgresql，参数模板名称和描述自定义。

Input: 

```
tccli postgres CreateParameterTemplate --cli-unfold-argument  \
    --TemplateName test_template \
    --DBMajorVersion 13 \
    --DBEngine postgresql \
    --TemplateDescription test
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90",
        "TemplateId": "497857b4-4676-5583-8359-b697fe5968d9"
    }
}
```

