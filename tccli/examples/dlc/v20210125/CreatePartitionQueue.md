**Example 1: 新增资源队列**



Input: 

```
tccli dlc CreatePartitionQueue --cli-unfold-argument  \
    --PartitionCode dlc-p-ofvhyjzn \
    --QueueName 122211 \
    --ResourceUsages.0.ResourceSpec.ResourceType 1 \
    --ResourceUsages.0.ResourceSpec.InstanceType 1 \
    --ResourceUsages.0.ResourceSpec.BillingItem 2 \
    --ResourceUsages.0.ResourceSpec.SpecDesc 2 \
    --ResourceUsages.0.ResourceSpec.Spec 1 \
    --ResourceUsages.0.Min 1 \
    --ResourceUsages.0.Max 11 \
    --QueueType 1 \
    --Description 1
```

Output: 
```
{
    "Response": {
        "Id": 140,
        "RequestId": "298077fc-eb59-46d3-8149-767329913006"
    }
}
```

