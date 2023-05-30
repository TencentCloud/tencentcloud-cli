**Example 1: 查询CBS可用容量**



Input: 

```
tccli tocservice QueryApplyCBSCapacity --cli-unfold-argument  \
    --DeptId 102 \
    --Zone ap-guangzhou-5 \
    --DiskType CLOUD_PREMIUM \
    --DiskSize 100 \
    --DiskApplyNum 5 \
    --ProjectName 常规项目
```

Output: 
```
{
    "Response": {
        "Data": {
            "MaxNum": 10,
            "MaxInfo": [
                {
                    "KeyTitle": "云后端CBS容量计算可申领量",
                    "KeyValue": 100
                },
                {
                    "KeyTitle": "云规划最大剩余可用量",
                    "KeyValue": 10
                },
                {
                    "KeyTitle": "云梯单次提单数量上限",
                    "KeyValue": 100
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

