**Example 1: 创建云盘版本只读实例副本**

创建云盘版本只读实例副本

Input: 

```
tccli sqlserver CreateCloudReadOnlyDBInstances --cli-unfold-argument  \
    --InstanceId mssql-4cg9922v \
    --Zone ap-guangzhou-6 \
    --ReadOnlyGroupType 1 \
    --Memory 4 \
    --Storage 500 \
    --Cpu 2 \
    --MachineType CLOUD_HSSD \
    --ReadOnlyGroupForcedUpgrade 0
```

Output: 
```
{
    "Response": {
        "DealNames": [
            "202301231"
        ],
        "RequestId": "61999983-b0af-4889-b067-xxxxxxxxx"
    }
}
```

