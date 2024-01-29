**Example 1: 调整云数据库实例配置**

调整云数据库实例配置

Input: 

```
tccli mongodb ModifyDBInstanceSpec --cli-unfold-argument  \
    --InstanceId cmgo-p8vn**** \
    --Volume 250 \
    --Memory 4
```

Output: 
```
{
    "Response": {
        "RequestId": "d88095e5-50e8-4245-a0cf-993a536f9b20",
        "DealId": "7142863"
    }
}
```

**Example 2: 删除mognodb云数据库实例从节点**

广州二区和三区共删除2个从节点，最终节点数量变更为3

Input: 

```
tccli mongodb ModifyDBInstanceSpec --cli-unfold-argument  \
    --InstanceId cmgo-abcdef \
    --Memory 4 \
    --Volume 100 \
    --OplogSize 30 \
    --NodeNum 3 \
    --ReplicateSetNum 1 \
    --InMaintenance 1 \
    --RemoveNodeList.0.NodeName cmgo-3iecwbfx_0-node0 \
    --RemoveNodeList.0.Role SECONDARY \
    --RemoveNodeList.0.Zone ap-guangzhou-2 \
    --RemoveNodeList.1.NodeName cmgo-3iecwbfx_0-node1 \
    --RemoveNodeList.1.Role SECONDARY \
    --RemoveNodeList.1.Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "DealId": "7142863",
        "RequestId": "d88095e5-50e8-4245-a0cf-993a536f9b20"
    }
}
```

**Example 3: 新增mognodb云数据库实例从节点**

广州二区和三区共新增2个从节点，最终节点数量变更为5

Input: 

```
tccli mongodb ModifyDBInstanceSpec --cli-unfold-argument  \
    --InstanceId cmgo-abcdef \
    --Memory 4 \
    --Volume 100 \
    --OplogSize 30 \
    --NodeNum 5 \
    --ReplicateSetNum 1 \
    --InMaintenance 1 \
    --AddNodeList.0.Role SECONDARY \
    --AddNodeList.0.Zone ap-guangzhou-2 \
    --AddNodeList.1.Role SECONDARY \
    --AddNodeList.1.Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "DealId": "7142863",
        "RequestId": "d88095e5-50e8-4245-a0cf-993a536f9b20"
    }
}
```

