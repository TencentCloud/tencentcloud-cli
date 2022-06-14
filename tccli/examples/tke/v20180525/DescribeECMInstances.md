**Example 1: 获取实例相关信息**

获取实例相关信息

Input: 

```
tccli tke DescribeECMInstances --cli-unfold-argument  \
    --ClusterID cls-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "187c16d5-1f53-4e88-b684-077f0c7369b2",
        "TotalCount": 2,
        "InstanceInfoSet": [
            "info1",
            "info2"
        ]
    }
}
```

