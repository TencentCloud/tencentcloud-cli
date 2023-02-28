**Example 1: 查询专用集群内cos的容量信息**

查询专用集群内cos的容量信息

Input: 

```
tccli cdc DescribeDedicatedClusterCosCapacity --cli-unfold-argument  \
    --DedicatedClusterId cluster-gbo27yc4
```

Output: 
```
{
    "Response": {
        "CosCapacity": {
            "TotalCapacity": 3394.92,
            "TotalFreeCapacity": 3367.41,
            "TotalUsedCapacity": 27.51
        },
        "RequestId": "41aa48c2-477b-43c0-9d93-04ef3f529e5f"
    }
}
```

