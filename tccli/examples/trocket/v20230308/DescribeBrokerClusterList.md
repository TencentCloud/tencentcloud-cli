**Example 1: 查询共享集群列表**

查询共享集群列表

Input: 

```
tccli trocket DescribeBrokerClusterList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "RequestId": "1d0f0115-d77a-47eb-8ca5-2b930b3977e7",
    "Response": {
        "ClusterList": [
            {
                "ClusterName": "rmqbroker-cd-room1",
                "ComputeClusterCount": 18,
                "Labels": [],
                "Overselling": 587,
                "Available": true,
                "Room": "rmqnamsrv-cd-1"
            }
        ],
        "RequestId": "1d0f0115-d77a-47eb-8ca5-2b930b3977e7",
        "TotalCount": 1
    }
}
```

