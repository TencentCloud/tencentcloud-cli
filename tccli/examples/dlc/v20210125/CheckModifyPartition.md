**Example 1: 变配校验**



Input: 

```
tccli dlc CheckModifyPartition --cli-unfold-argument  \
    --PartitionCode dlc-p-ofvhyjzn \
    --TargetResourceQuotaList.0.ResourceSpec.BillingItem sv_dlc_standard_cu_standard_cu \
    --TargetResourceQuotaList.0.Quota 1
```

Output: 
```
{
    "Response": {
        "CanModify": false,
        "MessageList": [
            {
                "BillingItem": "sv_dlc_standard_cu_standard_cu",
                "Message": "[sv_dlc_standard_cu_standard_cu]缩容需要释放191，但default队列仅有min=4可释放，不足187"
            }
        ],
        "RequestId": "57f96148-6c60-470e-9874-021444328acc"
    }
}
```

