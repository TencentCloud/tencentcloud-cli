**Example 1: 更新 API 密钥状态为禁用**

更新 API 密钥状态为禁用

Input: 

```
tccli tokenhub ModifyApiKeyStatus --cli-unfold-argument  \
    --ApiKeyId ak-20260325-xxxxxx \
    --Platform maas \
    --Status disable
```

Output: 
```
{
    "Response": {
        "RequestId": "0f2e294c-6c10-4ff6-8165-c25b3c5d21e0"
    }
}
```

