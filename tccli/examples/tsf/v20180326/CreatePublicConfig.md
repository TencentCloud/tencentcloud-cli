**Example 1: 创建公共配置项**



Input: 

```
tccli tsf CreatePublicConfig --cli-unfold-argument  \
    --ConfigName testconfig \
    --ConfigVersion 1.3 \
    --ConfigValue tsf.inventory.password.encrypt2:%20ENC(3M7wGw2XtFc5Y+rxOgNBLrm2spUtgodjIxa+7F3XcAo
```

Output: 
```
{
    "Response": {
        "RequestId": "3d600e1f-87c3-4aa6-afa5-a4f8330fa181",
        "Result": true
    }
}
```

