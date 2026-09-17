**Example 1: DescribePartitionQueues**



Input: 

```
tccli dlc DescribePartitionQueues --cli-unfold-argument  \
    --PartitionCode dlc-p-bazbypwy \
    --Page 1 \
    --PageSize 11
```

Output: 
```
{
    "Response": {
        "DefaultQueue": {
            "Id": 121,
            "IsDefault": 1,
            "QueueName": "default",
            "ResourceUsage": [
                {
                    "Max": 32,
                    "Min": 32,
                    "ResourceSpec": {
                        "BillingItem": "sv_dlc_standard_cu_standard_cu",
                        "InstanceType": "",
                        "ResourceType": "CPU",
                        "Spec": "0:1:4",
                        "SpecDesc": "1CPU / 4GB"
                    }
                }
            ],
            "ResourceQuotas": [
                {
                    "ResourceType": "CU",
                    "Unit": "core",
                    "Total": 32.0,
                    "Used": 10.0,
                    "Available": 22.0
                }
            ]
        },
        "QueueList": [
            {
                "Id": 121,
                "IsDefault": 1,
                "QueueName": "default",
                "ResourceUsage": [
                    {
                        "Max": 32,
                        "Min": 32,
                        "ResourceSpec": {
                            "BillingItem": "sv_dlc_standard_cu_standard_cu",
                            "InstanceType": "",
                            "ResourceType": "CPU",
                            "Spec": "0:1:4",
                            "SpecDesc": "1CPU / 4GB"
                        }
                    }
                ],
                "ResourceQuotas": [
                    {
                        "ResourceType": "CU",
                        "Unit": "core",
                        "Total": 32.0,
                        "Used": 10.0,
                        "Available": 22.0
                    }
                ]
            }
        ],
        "Total": 2,
        "RequestId": "4e1e0c64-d54d-4669-8076-dd0cde9c1754"
    }
}
```

