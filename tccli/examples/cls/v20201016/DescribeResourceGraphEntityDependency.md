**Example 1: 查询资源拓扑关系**



Input: 

```
tccli cls DescribeResourceGraphEntityDependency --cli-unfold-argument  \
    --ResourceGraphId test-yunapi-full \
    --EntityId 002b693f4f8cd075e2c6a750e6e58e2c \
    --Depth 1 \
    --Limit 3 \
    --FromTime 1782230000 \
    --ToTime 1782231000
```

Output: 
```
{
    "Response": {
        "Topology": {
            "Edges": [],
            "Nodes": [
                {
                    "Depth": 0,
                    "Domain": "k8s",
                    "EntityClassName": "k8s.pod",
                    "EntityId": "002b693f4f8cd075e2c6a750e6e58e2c",
                    "Name": "loadtest-pod-src-23-93",
                    "Product": "null"
                }
            ]
        },
        "RequestId": "e18c3587-d333-42cf-96dd-6319406f5bfc"
    }
}
```

