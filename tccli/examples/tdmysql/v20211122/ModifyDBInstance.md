**Example 1: 纵向变配**



Input: 

```
tccli tdmysql ModifyDBInstance --cli-unfold-argument  \
    --InstanceId tdsql3-7d3ymevo4z \
    --DryRun False \
    --HybridNodeCpu 2 \
    --HybridNodeMem 4 \
    --HybridNodeNum 3 \
    --Disk 30 \
    --SpecCode 2c4g
```

Output: 
```
{
    "Response": {
        "FlowId": 110149,
        "RequestId": "2340d9d0-5e20-46a6-8078-eece8d2d46a0"
    }
}
```

**Example 2: 预检查变配计划（DryRun模式）**

预检查变配计划，不实际执行变配，返回变配方式和子流程编排描述

Input: 

```
tccli tdmysql ModifyDBInstance --cli-unfold-argument  \
    --InstanceId tdsql3-ecab00ac \
    --HybridNodeCpu 16 \
    --HybridNodeMem 32 \
    --Disk 8000 \
    --HybridNodeNum 20 \
    --DryRun True
```

Output: 
```
{
    "Response": {
        "IsInPlaceModification": false,
        "IsMigrateModification": true,
        "ModifyPlan": "纵向变配: 规格 4c8g -> 16c32g, 磁盘 500GB -> 8000GB; 横向变配: 节点数 6 -> 20",
        "RequestId": "5b104d05-7e16-4869-87fe-dbd2e8f30b70"
    }
}
```

