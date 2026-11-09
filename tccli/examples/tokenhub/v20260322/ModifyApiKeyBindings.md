**Example 1: 更新 API 密钥绑定。**

更新API 密钥的绑定类型BindType 为 all ， Bindings 为空，即模型和服务全选

Input: 

```
tccli tokenhub ModifyApiKeyBindings --cli-unfold-argument  \
    --ApiKeyId ak-20260323-xxxxxx \
    --Platform maas \
    --BindType all
```

Output: 
```
{
    "Response": {
        "RequestId": "396579c9-cfee-479b-9475-76b2614cc3c0"
    }
}
```

