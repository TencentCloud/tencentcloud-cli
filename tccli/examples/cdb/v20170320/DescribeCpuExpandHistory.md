**Example 1: 用于查询扩容历史**



Input: 

```
tccli cdb DescribeCpuExpandHistory --cli-unfold-argument  \
    --EndTime 1744006585 \
    --InstanceId cdb-1yjb41f3 \
    --Limit 20 \
    --Offset 0 \
    --StartTime 1743920185
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "EndTime": 1743696012,
                "Error": "",
                "ExpandType": "auto",
                "ExtendCPUNum": 2,
                "NewCpu": 6,
                "OldCpu": 8,
                "OperationType": "reduce",
                "StartTime": 1743696005
            }
        ],
        "RequestId": "32ae2a3d-2c59-4115-942a-2620dd9d5d07",
        "TotalCount": 10
    }
}
```

