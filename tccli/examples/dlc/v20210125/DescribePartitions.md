**Example 1: DescribePartitions**



Input: 

```
tccli dlc DescribePartitions --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Partitions": [
            {
                "Name": "asfas",
                "PartitionCode": "dlc-p-ogwlzmvs",
                "PayMode": 1,
                "QueueCount": 1,
                "ResourceQuota": [
                    {
                        "Quota": 32,
                        "ResourceSpec": {
                            "BillingItem": "sv_dlc_standard_cu_standard_cu",
                            "InstanceType": "",
                            "ResourceType": "CPU"
                        }
                    }
                ],
                "Status": 11,
                "UpdateTime": "2026-03-19T15:12:19"
            }
        ],
        "Total": 10,
        "RequestId": "8160ca16-3a24-4779-a75c-d8e2e453815f"
    }
}
```

