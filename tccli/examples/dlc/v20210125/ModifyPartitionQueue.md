**Example 1: ModifyPartitionQueue**



Input: 

```
tccli dlc ModifyPartitionQueue --cli-unfold-argument  \
    --PartitionCode partition-mock-001 \
    --QueueName data-etl \
    --ResourceUsages.0.ResourceSpec.ResourceType 1 \
    --ResourceUsages.0.ResourceSpec.InstanceType 2 \
    --ResourceUsages.0.ResourceSpec.BillingItem 1 \
    --ResourceUsages.0.Min 0 \
    --ResourceUsages.0.Max 0 \
    --Id 12 \
    --Description 33
```

Output: 
```
{
    "Response": {
        "RequestId": "2d46b441-2315-4381-ae5c-62e64fd3bb10"
    }
}
```

