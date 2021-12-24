**Example 1: DescribeEdgeUnitApplicationPodContainers**



Input: 

```
tccli iecp DescribeEdgeUnitApplicationPodContainers --cli-unfold-argument  \
    --ApplicationId 1 \
    --EdgeUnitId 1 \
    --PodName Pod
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "ContainerSet": []
    }
}
```

