**Example 1: 请求示例**

设置加密密钥

Input: 

```
tccli drm CreateEncryptKeys --cli-unfold-argument  \
    --DrmType FAIRPLAY \
    --ContentType LiveVideo \
    --ContentId set_example \
    --Keys.0.Track HD \
    --Keys.0.KeyId 12345678901234567890123456789015 \
    --Keys.0.Key dlAuJ6EKsKVMKS/atJpxRUEwBjdDHSmDcRk/fDk+5PdaLQq7Bq9a8d5XitcoYWYZ9ukzzhYT0oTqhTbFUfboKEL7iAhJ7SvWgVMwAlPgcV+ZgA2/AH8Xvj8Y+iOb3sN+oy3thGGW71+GxAFNXG46HB0MWWvA15KBTfA+f42eVcs
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

