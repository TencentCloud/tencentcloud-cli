**Example 1: 查询指定集群节点概览信息。**

查询指定集群节点概览信息，集群ID为hpc-ggaqjyax。

Input: 

```
tccli thpc DescribeNodes --cli-unfold-argument  \
    --ClusterId hpc-ggaqjyax \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "InstanceId": "ins-j3n6kiae",
                "Zone": "ap-chongqing-1",
                "NodeState": "RUNNING",
                "ImageId": "img-l8og963d",
                "QueueName": "compute",
                "NodeRole": "Compute",
                "NodeType": "DYNAMIC"
            }
        ],
        "TotalCount": 3,
        "RequestId": "6793673e-3bce-4fbb-adea-923a82267da2"
    }
}
```

