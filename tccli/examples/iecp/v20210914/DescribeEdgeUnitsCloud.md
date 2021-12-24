**Example 1: 示例**



Input: 

```
tccli iecp DescribeEdgeUnitsCloud --cli-unfold-argument  \
    --NamePattern  \
    --Limit 10 \
    --Order  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "35ce2926-eea5-4b6d-b03b-e25abefb28e8",
        "TotalCount": 1,
        "EdgeUnitSet": [
            {
                "EdgeId": 2,
                "ClusterId": "cls-lny263r1",
                "Region": "ap-beijing",
                "ClusterName": "logossss",
                "K8SVersion": "1.16.7",
                "PodCIDR": "10.1.0.0/16",
                "ServiceCIDR": "10.2.0.0/16",
                "VpcId": "vpc-44crlhxe",
                "ClusterDesc": "字符串",
                "Status": "Running",
                "CreateTime": "2021-10-09 11:05:18",
                "EdgeClusterVersion": "2.2"
            }
        ]
    }
}
```

**Example 2: 获取边缘集群列表**



Input: 

```
tccli iecp DescribeEdgeUnitsCloud --cli-unfold-argument  \
    --NamePattern  \
    --Limit 10 \
    --Order  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "fa5f617e-36b4-499a-bb4f-b6ed5269780e",
        "TotalCount": 1,
        "EdgeUnitSet": [
            {
                "EdgeId": 2,
                "ClusterId": "cls-lny263r1",
                "Region": "ap-beijing",
                "ClusterName": "logossss",
                "K8SVersion": "1.16.7",
                "PodCIDR": "10.1.0.0/16",
                "ServiceCIDR": "10.2.0.0/16",
                "VpcId": "vpc-44crlhxe",
                "ClusterDesc": "字符串",
                "Status": "Running",
                "CreateTime": "2021-10-09 11:05:18",
                "EdgeClusterVersion": "2.2"
            }
        ]
    }
}
```

