**Example 1: 获取迁移校验结果**

校验成功

Input: 

```
tccli dts DescribeMigrateCheckJob --cli-unfold-argument  \
    --JobId dts-dau5czmd
```

Output: 
```
{
    "Response": {
        "Status": "finished",
        "ErrorCode": 0,
        "ErrorMessage": "ok",
        "Progress": "100",
        "CheckFlag": 1,
        "RequestId": "336448b0-2a45-4be4-8356-c245eab5784f"
    }
}
```

**Example 2: 获取迁移校验结果-2**

校验失败

Input: 

```
tccli dts DescribeMigrateCheckJob --cli-unfold-argument  \
    --JobId dts-1kl0iy0v
```

Output: 
```
{
    "Response": {
        "Status": "finished",
        "ErrorCode": -1,
        "ErrorMessage": "选择的库表不存在，请重新选择[存在输入参数table在源实例没有找到]",
        "Progress": "100",
        "CheckFlag": 0,
        "RequestId": "67b4cfcf-6957-48ae-b7ef-ba33209895e3"
    }
}
```

