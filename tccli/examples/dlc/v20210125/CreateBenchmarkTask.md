**Example 1: 测试**



Input: 

```
tccli dlc CreateBenchmarkTask --cli-unfold-argument  \
    --ServiceId svc-20260617111616-a3ol \
    --ResourcePartitionId dlc-p-jhzmcfna \
    --Queue default \
    --BillingItem sv_dlc_standard_cu_standard_cu \
    --Spec 2
```

Output: 
```
{
    "Response": {
        "AppId": 260200066,
        "CreateTime": 1784862009898,
        "DeploymentResources": [],
        "InputTokens": 256,
        "MaxConcurrency": 16,
        "OutputTokens": 1024,
        "RequestsPerSecond": 5,
        "Resources": {
            "BillingItem": "sv_dlc_standard_cu_standard_cu",
            "Queue": "default",
            "ResourcePartitionId": "dlc-p-jhzmcfna",
            "Spec": 2
        },
        "ServiceId": "svc-20260617111616-a3ol",
        "ServiceName": "dlc_mao_0617",
        "Status": "Pending",
        "SubAccountUin": "700002655694",
        "TaskId": "bench-20260724110009-h4wb",
        "TaskName": "benchmark-dlc_mao_0617-1784862009876",
        "TotalPrompts": 200,
        "Uin": "700002655694",
        "UpdateTime": 1784862009898,
        "UseGateway": true,
        "RequestId": "46dd3a6a-3c50-4c4e-b48b-67a77be7568c"
    }
}
```

