**Example 1: 查询tke集群接入情况**



Input: 

```
tccli cls DescribeResourceGraphTkeClusterStatus --cli-unfold-argument  \
    --ClusterIds cls-3jcth2i3
```

Output: 
```
{
    "Response": {
        "ConnectedClusterInfos": [
            {
                "ClusterId": "cls-3jcth2i3",
                "ResourceGraphId": "29a76d21-8e44-4d35-928f-4987c4b333ea",
                "ResourceGraphName": "test-han-1",
                "TaskId": "b00500c0-98dd-4c1d-a766-0ce1b7a0dc6d",
                "TaskName": "tke"
            }
        ],
        "UnconnectedClusterIds": [],
        "RequestId": "40ed8a93-6431-4f4c-86e8-189501f12b13"
    }
}
```

