**Example 1: 创建配置项**



Input: 

```
tccli tsf CreateConfig --cli-unfold-argument  \
    --ApplicationId application-gyq2xry5 \
    --ConfigName test_openapi_config \
    --ConfigVersion v1.0 \
    --ConfigValue 'api.invok.limit: 5000'
```

Output: 
```
{
    "Response": {
        "RequestId": "8007ea57-6d26-43db-aa75-ad72cb3669ca",
        "Result": true
    }
}
```

