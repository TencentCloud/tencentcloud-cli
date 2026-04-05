**Example 1: 添加模型服务鉴权**



Input: 

```
tccli wedata CreateModelServiceAuthToken --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --ServiceGroupId 960ed2fc-f40e-4b34-b662-a3ed689e035b \
    --Name test_abc \
    --Description aaaa_111
```

Output: 
```
{
    "Response": {
        "Data": {
            "TiOneRequestId": "1b0d04f5-80be-4e79-9cf7-84b065031017"
        },
        "RequestId": "d5a5ea14-ebcf-40ef-8424-0e898901e7b4"
    }
}
```

