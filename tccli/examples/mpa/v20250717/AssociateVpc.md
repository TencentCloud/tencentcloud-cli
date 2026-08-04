**Example 1: 关联VPC**



Input: 

```
tccli mpa AssociateVpc --cli-unfold-argument  \
    --AgentAcceleratorId aat-a8kx2ye5 \
    --VpcInfo.0.VpcId vpc-gmjjk6sn \
    --VpcInfo.0.VpcRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "TaskId": "47dbbb6d-9df5-4549-94cc-065f54dada14",
        "RequestId": "82f917b9-902e-4a5b-99ef-32e6fa402c0f"
    }
}
```

