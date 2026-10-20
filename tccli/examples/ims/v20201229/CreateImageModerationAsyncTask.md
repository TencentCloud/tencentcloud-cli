**Example 1: 创建异步审核任务示例**

创建异步审核任务示例

Input: 

```
tccli ims CreateImageModerationAsyncTask --cli-unfold-argument  \
    --BizType TencentCloudDefault \
    --FileUrl https://test.jpg \
    --DataId a61237dd-c2a0-43e7-a3da-d27022d39ba7 \
    --CallbackUrl https://callback.example.com/tencnet/callback \
    --Type IMAGE
```

Output: 
```
{
    "Response": {
        "RequestId": "193101e1-e9b6-4a9b-b29e-6e37db58beef",
        "DataId": "a61237dd-c2a0-43e7-a3da-d27022d39ba7"
    }
}
```

