**Example 1: 创建公共配置项**



Input: 

```
tccli tsf CreatePublicConfig --cli-unfold-argument  \
    --ConfigName config_pub_app \
    --ConfigVersion v1 \
    --ConfigVersionDesc This is desc \
    --ConfigValue config: enabled \
    --ConfigType public \
    --EncodeWithBase64 True \
    --ProgramIdList program-6a79x94v
```

Output: 
```
{
    "Response": {
        "RequestId": "a1563762-2470-42d0-a35f-6a03a05d2457",
        "Result": true
    }
}
```

