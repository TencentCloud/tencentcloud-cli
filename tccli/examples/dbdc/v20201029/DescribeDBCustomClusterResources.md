**Example 1: 查询集群的资源分配信息**

本接口（DescribeDBCustomClusterResources）用户查询DB Custom 集群的资源分配详情

Input: 

```
tccli dbdc DescribeDBCustomClusterResources --cli-unfold-argument  \
    --ClusterId dbcc-sizxd0hi
```

Output: 
```
{
    "Response": {
        "Allocatable": {
            "Cpu": 3.86,
            "Memory": 2.572,
            "Pods": 506
        },
        "Available": {
            "Cpu": 3.6,
            "Memory": 2.387,
            "Pods": 494
        },
        "Capacity": {
            "Cpu": 4,
            "Memory": 3.768,
            "Pods": 506
        },
        "Limits": {
            "Cpu": 15.2,
            "Memory": 14.763,
            "Pods": 0
        },
        "NodeCount": 2,
        "Requests": {
            "Cpu": 0.26,
            "Memory": 0.186,
            "Pods": 12
        },
        "RequestId": "98a6ae66-bfb9-4515-83ce-36f163cb59f9"
    }
}
```

