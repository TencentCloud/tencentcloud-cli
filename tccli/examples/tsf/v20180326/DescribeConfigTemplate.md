**Example 1: 导入配置模板**



Input: 

```
tccli tsf DescribeConfigTemplate --cli-unfold-argument  \
    --ConfigTemplateId dcfg_temp-vwkjqd6v
```

Output: 
```
{
    "Response": {
        "RequestId": "3a358065-d0c6-401b-8bc5-a38ebccac39e",
        "Result": {
            "ConfigTemplateDesc": "",
            "ConfigTemplateId": "dcfg_temp-vwkjqd6v",
            "ConfigTemplateName": "garden-test",
            "ConfigTemplateType": "Ribbon",
            "ConfigTemplateValue": "#请求处理超时时间\nribbon.ReadTimeout: 5000\n#请求连接超时时间\nribbon.ConnectTimeout: 2000\n",
            "CreateTime": "2022-08-23 15:44:11",
            "UpdateTime": null
        }
    }
}
```

