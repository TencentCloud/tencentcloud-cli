**Example 1: 查询纳管预检查结果**



Input: 

```
tccli tione DescribeBillingInstanceSemiCheckTask --cli-unfold-argument  \
    --ResourceGroupId rsg-n7b2xxp8 \
    --TaskId 6d90910b-7b0c-4009-af8e-e91c243e22ee
```

Output: 
```
{
    "Response": {
        "TaskId": "6d90910b-7b0c-4009-af8e-e91c243e22ee",
        "ResourceGroupId": "rsg-n7b2xxp8",
        "ChargeType": "PREPAID",
        "Status": "COMPLETED",
        "StartTime": "2025-12-16 20:22:52",
        "EndTime": "2025-12-16 20:22:53",
        "TotalCount": "5",
        "Results": [
            {
                "CVMInstanceId": "ins-opmdecy7",
                "Valid": false,
                "RejectedInfos": [
                    {
                        "Code": "InstanceNotFound",
                        "Reason": "InstanceNotFound"
                    },
                    {
                        "Code": "UnknownError",
                        "Reason": "UnknownError"
                    }
                ]
            },
            {
                "CVMInstanceId": "ins-c2ffftk1",
                "Valid": false,
                "RejectedInfos": [
                    {
                        "Code": "InstanceNotFound",
                        "Reason": "InstanceNotFound"
                    },
                    {
                        "Code": "UnknownError",
                        "Reason": "UnknownError"
                    }
                ]
            },
            {
                "CVMInstanceId": "ins-h856t0br",
                "Valid": true,
                "RejectedInfos": []
            },
            {
                "CVMInstanceId": "ins-kubmemq1",
                "Valid": true,
                "RejectedInfos": []
            },
            {
                "CVMInstanceId": "ins-gzxycqrn",
                "Valid": true,
                "RejectedInfos": []
            }
        ],
        "RequestId": "99418420-6454-4420-84d2-40f532ee07e8"
    }
}
```

