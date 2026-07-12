**Example 1: ModifyApiKeyInfo 更新 API 密钥备注信息**

 更新 API 密钥备注信息为“test-new-remark”

Input: 

```
tccli tokenhub ModifyApiKeyInfo --cli-unfold-argument  \
    --ApiKeyId ak-20260320-a1b2c3d4 \
    --Platform maas \
    --Remark test-new-remark
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdaaab-2aa3-4e03-87fb-795cf37b2079"
    }
}
```

