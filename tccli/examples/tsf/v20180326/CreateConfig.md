**Example 1: 创建配置项**



Input: 

```
tccli tsf CreateConfig --cli-unfold-argument  \
    --ConfigName config_app \
    --ConfigVersion v1 \
    --ConfigVersionDesc This is desc \
    --ConfigValue config: enabled \
    --ApplicationId application-5yr26r9a \
    --ConfigType application \
    --EncodeWithBase64 True \
    --ProgramIdList program-6a79x94v
```

Output: 
```
{
    "Response": {
        "RequestId": "fa979523-5509-4073-89b8-65c2bf86ff9a",
        "Result": true
    }
}
```

