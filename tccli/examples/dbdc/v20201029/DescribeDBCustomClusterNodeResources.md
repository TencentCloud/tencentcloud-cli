**Example 1: 查询节点资源情况**



Input: 

```
tccli dbdc DescribeDBCustomClusterNodeResources --cli-unfold-argument  \
    --ClusterId dbcc-n9ku9uyc \
    --NodeIds dbcn-1qaik21r
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "Allocatable": {
                    "Cpu": 1.93,
                    "Memory": 1.286,
                    "Pods": 253
                },
                "Available": {
                    "Cpu": 1.8,
                    "Memory": 1.193,
                    "Pods": 247
                },
                "Capacity": {
                    "Cpu": 2,
                    "Memory": 1.884,
                    "Pods": 253
                },
                "Limits": {
                    "Cpu": 7.6,
                    "Memory": 7.382,
                    "Pods": 0
                },
                "NodeId": "dbcn-1qaik21r",
                "Requests": {
                    "Cpu": 0.13,
                    "Memory": 0.093,
                    "Pods": 6
                }
            }
        ],
        "RequestId": "29117a44-6bc0-4ab9-b667-7f8c5b322a1f"
    }
}
```

