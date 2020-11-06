**Example 1: Querying GN2 Series Models in Guangzhou Zone 3**



Input: 

```
tccli batch DescribeAvailableCvmInstanceTypes --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-3 \
    --Filters.1.Name instance-family \
    --Filters.1.Values GN2
```

Output: 
```
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "Mem": 56,
                "Cpu": 28,
                "InstanceType": "GN2.7XLARGE56",
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "GN2"
            },
            {
                "Mem": 112,
                "Cpu": 56,
                "InstanceType": "GN2.14XLARGE112",
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "GN2"
            }
        ],
        "RequestId": "59f5b671-c492-4536-bbed-e5fbf78619dd"
    }
}
```

