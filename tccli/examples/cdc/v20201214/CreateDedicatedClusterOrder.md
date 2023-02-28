**Example 1: 创建专用集群订单**

创建专用集群订单

Input: 

```
tccli cdc CreateDedicatedClusterOrder --cli-unfold-argument  \
    --DedicatedClusterId cluster-gbo27yc4 \
    --DedicatedClusterTypes.0.Id cluster-gbo27yc4 \
    --DedicatedClusterTypes.0.Count 1 \
    --CosInfo.Size 1 \
    --CosInfo.Type COS \
    --CbsInfo.Size 1 \
    --CbsInfo.Type SSD
```

Output: 
```
{
    "Response": {
        "DedicatedClusterOrderId": "ord-0yq4a8ia",
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

