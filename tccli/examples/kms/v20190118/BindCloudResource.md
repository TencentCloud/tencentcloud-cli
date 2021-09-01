**Example 1: 绑定密钥和云产品资源的使用关系**

绑定密钥和云产品资源的使用关系

Input: 

```
tccli kms BindCloudResource --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01 \
    --ProductId ssm \
    --ResourceId resourceId
```

Output: 
```
{
    "Response": {
        "RequestId": "fe11aa29-0cc2-4204-bfea-6ebb30cc00d7"
    }
}
```

