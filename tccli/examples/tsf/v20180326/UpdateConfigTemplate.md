**Example 1: 更新参数模板**



Input: 

```
tccli tsf UpdateConfigTemplate --cli-unfold-argument  \
    --ConfigTemplateId dcfg_temp-aln5d3wv \
    --ConfigTemplateName app_config \
    --ConfigTemplateDesc This is desc \
    --ConfigTemplateType Ribbon \
    --ConfigTemplateValue #请求处理超时时间\nribbon.ReadTimeout: 5000\n#请求连接超时时间\nribbon.ConnectTimeout: 2000\n#同一实例最大重试次数，不包括首次调用\nribbon.MaxAutoRetries: 0\n#重试其他实例的最大重试次数，不包括首次所选的server\nribbon.MaxAutoRetriesNextServer: 1\n#是否对所有操作请求都进行重试\nribbon.OkToRetryOnAllOperations: false\n
```

Output: 
```
{
    "Response": {
        "RequestId": "b624eb9f-8bdb-440e-b875-e540d9186b7b",
        "Result": true
    }
}
```

