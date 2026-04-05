**Example 1: 查询 TIONE 资源组**



Input: 

```
tccli wedata ListTiOneBillingResourceGroups --cli-unfold-argument  \
    --SearchWord create
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceGroupSet": [
                {
                    "FreeInstance": 3,
                    "InstanceSet": [
                        {
                            "AutoRenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                            "CreateTime": "2025-07-18 14:34:25",
                            "CvmInstanceId": "ins-b04wtlpi",
                            "ErrCode": "",
                            "ErrMsg": "",
                            "ExpireTime": "2025-08-18 14:34:25",
                            "InstanceId": "sm-5x6vtmw7",
                            "InstanceStatus": "RUNNING",
                            "IsSWFinished": false,
                            "SpecAlias": "4C8GB S6",
                            "SpecFeatures": [],
                            "SpecId": "sv_tio_platform_cloud_pre_cpu_4c8g_s6_sw",
                            "SubUin": "100036988056",
                            "TotalResource": {
                                "Cpu": 3900,
                                "Gpu": 0,
                                "GpuType": "",
                                "Memory": 5831,
                                "RealGpu": 0,
                                "RealGpuDetailSet": []
                            },
                            "UsedResource": {
                                "Cpu": 0,
                                "Gpu": 0,
                                "GpuType": "",
                                "Memory": 0,
                                "RealGpu": 0,
                                "RealGpuDetailSet": []
                            }
                        },
                        {
                            "AutoRenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                            "CreateTime": "2025-07-18 14:34:25",
                            "CvmInstanceId": "ins-ocw0fbrc",
                            "ErrCode": "",
                            "ErrMsg": "",
                            "ExpireTime": "2025-08-18 14:34:25",
                            "InstanceId": "sm-kh74zvpw",
                            "InstanceStatus": "RUNNING",
                            "IsSWFinished": false,
                            "SpecAlias": "4C8GB S6",
                            "SpecFeatures": [],
                            "SpecId": "sv_tio_platform_cloud_pre_cpu_4c8g_s6_sw",
                            "SubUin": "100036988056",
                            "TotalResource": {
                                "Cpu": 3900,
                                "Gpu": 0,
                                "GpuType": "",
                                "Memory": 5831,
                                "RealGpu": 0,
                                "RealGpuDetailSet": []
                            },
                            "UsedResource": {
                                "Cpu": 1000,
                                "Gpu": 0,
                                "GpuType": "",
                                "Memory": 1024,
                                "RealGpu": 0,
                                "RealGpuDetailSet": []
                            }
                        },
                        {
                            "AutoRenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                            "CreateTime": "2025-07-18 14:34:25",
                            "CvmInstanceId": "ins-ryk1irqm",
                            "ErrCode": "",
                            "ErrMsg": "",
                            "ExpireTime": "2025-08-18 14:34:25",
                            "InstanceId": "sm-p9k62qff",
                            "InstanceStatus": "RUNNING",
                            "IsSWFinished": false,
                            "SpecAlias": "4C8GB S6",
                            "SpecFeatures": [],
                            "SpecId": "sv_tio_platform_cloud_pre_cpu_4c8g_s6_sw",
                            "SubUin": "100036988056",
                            "TotalResource": {
                                "Cpu": 3900,
                                "Gpu": 0,
                                "GpuType": "",
                                "Memory": 5831,
                                "RealGpu": 0,
                                "RealGpuDetailSet": []
                            },
                            "UsedResource": {
                                "Cpu": 0,
                                "Gpu": 0,
                                "GpuType": "",
                                "Memory": 0,
                                "RealGpu": 0,
                                "RealGpuDetailSet": []
                            }
                        }
                    ],
                    "ResourceGroupId": "rsg-v99ddsdk",
                    "ResourceGroupName": "test_create_to_cvm",
                    "TagSet": [],
                    "TotalInstance": 3,
                    "TotalResource": {
                        "Cpu": 11700,
                        "Gpu": 0,
                        "GpuDetailSet": [],
                        "Memory": 17493
                    },
                    "UsedResource": {
                        "Cpu": 1000,
                        "Gpu": 0,
                        "GpuDetailSet": [],
                        "Memory": 1024
                    }
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "4f485f5e-8f61-4577-9cbd-b05e96c4d840"
    }
}
```

