**Example 1: 配置模板创建**



Input: 

```
tccli tsf CreateConfigTemplate --cli-unfold-argument  \
    --ConfigTemplateName 配置1 \
    --ConfigTemplateDesc 11111111111 \
    --ConfigTemplateType Ribbon \
    --ConfigTemplateValue '#请求处理超时时间
ribbon.ReadTimeout: 5000
#请求连接超时时间
ribbon.ConnectTimeout: 2000
#同一实例最大重试次数，不包括首次调用
ribbon.MaxAutoRetries: 0
#重试其他实例的最大重试次数，不包括首次所选的server
ribbon.MaxAutoRetriesNextServer: 1
#是否对所有操作请求都进行重试
ribbon.OkToRetryOnAllOperations: false'
```

Output: 
```
{
    "Response": {
        "RequestId": "841f10d8-24e7-471b-ad8a-b401d9dcbe70",
        "Result": true
    }
}
```

