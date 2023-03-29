**Example 1: 导出获取区域主机列表**

本接口 (DescribeExportMachines) 用于导出区域主机列表。

Input: 

```
tccli cwp DescribeExportMachines --cli-unfold-argument  \
    --MachineType CVM \
    --MachineRegion ap-shanghai \
    --Filters.0.Name Keywords \
    --Filters.0.Values 10.0.1.1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TaskId": "123",
        "RequestId": "c30f35cb-2f3e-94f5-59ae-316e0f32e660"
    }
}
```

