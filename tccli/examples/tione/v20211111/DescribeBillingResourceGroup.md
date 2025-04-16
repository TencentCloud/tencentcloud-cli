**Example 1: 查询资源组节点列表**



Input: 

```
tccli tione DescribeBillingResourceGroup --cli-unfold-argument  \
    --ResourceGroupId ersg-9hw7jfk6 \
    --Filters.0.Name InstanceStatus \
    --Filters.0.Values RUNNING \
    --Filters.0.Negative True \
    --Filters.0.Fuzzy True \
    --Offset 1 \
    --Limit 1 \
    --Order ASC \
    --OrderField CreateTime
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceSet": [
            {
                "InstanceId": "sm-8r7jbnsz",
                "UsedResource": {
                    "Cpu": 78200,
                    "Memory": 349696,
                    "Gpu": 400,
                    "GpuType": "4090D",
                    "RealGpu": 0,
                    "RealGpuDetailSet": []
                },
                "TotalResource": {
                    "Cpu": 78200,
                    "Memory": 349780,
                    "Gpu": 400,
                    "GpuType": "4090D",
                    "RealGpu": 0,
                    "RealGpuDetailSet": []
                },
                "InstanceStatus": "RUNNING",
                "SubUin": "100023251204",
                "CreateTime": "2024-12-19 15:36:44",
                "ExpireTime": "",
                "AutoRenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "SpecId": "sv_tio_platform_cloud_post_gpu_80c368g_44090d_sw",
                "SpecAlias": "80核358GB 4090D*4"
            }
        ],
        "RequestId": "114e2564-3ce6-469c-b9c0-284a51247902"
    }
}
```

