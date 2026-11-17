**Example 1: 查询GPU资源组**

查询当前地域、当前租户的 GPU 资源组及统计。通过 resource-group-id 精确过滤可查询组详情，仍返回数组；无匹配项返回空数组。资源组可以为空，商业期限和续费标记逐台保存。

Input: 

```
tccli ags DescribeGPUResourceGroups --cli-unfold-argument  \
    --Filters.0.Name resource-group-name-like \
    --Filters.0.Values 推理 \
    --Filters.1.Name gpu-type \
    --Filters.1.Values 5090d \
    --Filters.2.Name gpu-num \
    --Filters.2.Values 2 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "ResourceGroups": [
            {
                "ResourceGroupId": "gpug-example",
                "Name": "推理服务",
                "Spec": {
                    "GPUType": "5090d",
                    "GPUTypeAlias": "NVIDIA RTX 5090 D",
                    "GPUMemoryGiB": 64,
                    "CPU": 64,
                    "Memory": 192,
                    "GPUNum": 2
                },
                "Statistics": {
                    "TotalCount": 10,
                    "AvailableCount": 5,
                    "AllocatedCount": 3,
                    "StateCounts": {
                        "Delivering": 1,
                        "Active": 8,
                        "Isolated": 1,
                        "Destroying": 0
                    }
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "request-example"
    }
}
```

**Example 2: 按资源组ID查询详情**

复用同一接口查询详情，没有独立的 DescribeGPUResourceGroup Action。

Input: 

```
tccli ags DescribeGPUResourceGroups --cli-unfold-argument  \
    --Filters.0.Name resource-group-id \
    --Filters.0.Values gpug-example
```

Output: 
```
{
    "Response": {
        "ResourceGroups": [
            {
                "ResourceGroupId": "gpug-example",
                "Name": "推理服务",
                "Spec": {
                    "GPUType": "5090d",
                    "GPUTypeAlias": "NVIDIA RTX 5090 D",
                    "GPUMemoryGiB": 64,
                    "CPU": 64,
                    "Memory": 192,
                    "GPUNum": 2
                },
                "Statistics": {
                    "TotalCount": 10,
                    "AvailableCount": 5,
                    "AllocatedCount": 3,
                    "StateCounts": {
                        "Delivering": 1,
                        "Active": 8,
                        "Isolated": 1,
                        "Destroying": 0
                    }
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "request-example"
    }
}
```

