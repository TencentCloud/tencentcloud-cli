**Example 1: 重置话机注册密码**



Input: 

```
tccli ccc ResetExtensionPassword --cli-unfold-argument  \
    --SdkAppId 140000000 \
    --ExtensionId 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "86a17f0e-bcb3-46bf-ac66-8f165fe52127",
        "Password": "xxxxxxxxxxxxxxxxx"
    }
}
```

