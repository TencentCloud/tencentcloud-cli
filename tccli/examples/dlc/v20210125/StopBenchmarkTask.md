**Example 1: 测试**



Input: 

```
tccli dlc StopBenchmarkTask --cli-unfold-argument  \
    --TaskId bench-20260616142301-vxcv
```

Output: 
```
{
    "Response": {
        "ApiKeyId": "apikey-20260616110430-f7i1",
        "ApiKeyName": "m-qwen2-tangbo-test-key-20260616110430-dznt",
        "AppId": 260200066,
        "CreateTime": 1781595798061,
        "InputTokens": 128,
        "MaxConcurrency": 2,
        "OutputTokens": 64,
        "RequestsPerSecond": 2,
        "ServiceId": "svc-20260616120346-s223",
        "ServiceName": "m-qwen2-tangbo-test-",
        "Status": "Stopped",
        "SubAccountUin": "700002655694",
        "TaskId": "bench-20260616142301-vxcv",
        "TaskName": "benchmark-m-qwen2-tangbo-test--1781590981220",
        "TotalPrompts": 5,
        "Uin": "700002655694",
        "UpdateTime": 1781595808406,
        "UseGateway": true,
        "RequestId": "16433bbf-29c4-4dd6-a819-f90af901da7f"
    }
}
```

