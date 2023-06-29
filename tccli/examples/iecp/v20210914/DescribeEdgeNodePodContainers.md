**Example 1: 查询节点Pod内的容器列表**



Input: 

```
tccli iecp DescribeEdgeNodePodContainers --cli-unfold-argument  \
    --EdgeUnitId 1 \
    --NodeId 1 \
    --PodName aaa-aa \
    --Namespace default
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "ContainerSet": [
            {
                "Name": "aaa-aa",
                "Id": "aaa",
                "Image": "nginx:latest",
                "CpuRequest": "250m",
                "CpuLimit": "500m",
                "MemoryRequest": "512Mi",
                "MemoryLimit": "1Gi",
                "RestartCount": 0,
                "Status": "Running"
            }
        ]
    }
}
```

