**Example 1: 修改白板应用任务相关配置**



Input: 

```
tccli tiw ModifyWhiteboardApplicationConfig --cli-unfold-argument  \
    --Configs.0.AdminUserId abcde \
    --Configs.0.BucketPrefix doc \
    --Configs.0.ResultDomain xxx \
    --Configs.0.AdminUserSig abcde \
    --Configs.0.Callback http://www.example.com/callback \
    --Configs.0.BucketName test-120000001 \
    --Configs.0.SdkAppId 1400000001 \
    --Configs.0.TaskType recording \
    --Configs.0.BucketLocation ap-guangzhou \
    --Configs.0.CallbackKey abcde \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

