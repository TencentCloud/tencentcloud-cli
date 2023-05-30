**Example 1: 查询可选的CBS类型**

查询可选的CBS类型

Input: 

```
tccli tocservice QueryCbsTypeInfo --cli-unfold-argument  \
    --DeptId 64 \
    --Zone ap-guangzhou-4 \
    --ObsProject 常规项目
```

Output: 
```
{
    "Response": {
        "RequestId": "1234567-1234-56712-34567",
        "Data": [
            {
                "DiskType": "CLOUD_PREMIUM",
                "DiskName": "高性能云硬盘"
            },
            {
                "DiskType": "CLOUD_SSD",
                "DiskName": "SSD云硬盘"
            }
        ]
    }
}
```

