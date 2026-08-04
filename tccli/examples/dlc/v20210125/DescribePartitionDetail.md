**Example 1: DescribePartitionDetail**



Input: 

```
tccli dlc DescribePartitionDetail --cli-unfold-argument  \
    --PartitionCode dlc-ae511d85
```

Output: 
```
{
    "Response": {
        "PartitionDetail": {
            "PartitionCode": "dlc-ae511d85",
            "PartitionName": "dlc-ae511d85",
            "PayMode": 1,
            "Region": 1,
            "ResourcePoolCode": "dlc-ae511d85_2",
            "Scheduler": "KUEUE",
            "Status": 1
        },
        "RequestId": "f11aa289-824c-42e9-b7b2-dca6ed75d9ba"
    }
}
```

