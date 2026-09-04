**Example 1: 测试**



Input: 

```
tccli dlc RerunBenchmarkTask --cli-unfold-argument  \
    --TaskId bench-20260616142301-vxcv
```

Output: 
```
{
    "Response": {
        "ApiKeyId": "apikey-20260616110430-f7i1",
        "ApiKeyName": "m-qwen2-tangbo-test-key-20260616110430-dznt",
        "AppId": 260200066,
        "CreateTime": 1781593674916,
        "InputTokens": 128,
        "MaxConcurrency": 2,
        "OutputTokens": 64,
        "RequestsPerSecond": 2,
        "ServiceId": "svc-20260616120346-s223",
        "ServiceName": "m-qwen2-tangbo-test-",
        "Status": "Pending",
        "SubAccountUin": "700002655694",
        "TaskId": "bench-20260616142301-vxcv",
        "TaskName": "benchmark-m-qwen2-tangbo-test--1781590981220",
        "TotalPrompts": 5,
        "Uin": "700002655694",
        "UpdateTime": 1781593674919,
        "UseGateway": true,
        "RequestId": "e1488fc7-1c69-4fcf-896f-a1e3401e34f8"
    }
}
```

