**Example 1: 查看计算环境创建信息列表**



Input: 

```
tccli batch DescribeComputeEnvCreateInfos --cli-unfold-argument  \
    --EnvIds env-lcx7qbbr \
    --Filters.1.Name env-id \
    --Filters.1.Values env-lcpcej85
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ComputeEnvCreateInfoSet": [
            {
                "EnvId": "env-lcx7qbbr",
                "EnvType": "MANAGED",
                "DesiredComputeNodeCount": 1,
                "EnvName": "batch-spot",
                "EnvDescription": "batch env ",
                "EnvData": {
                    "ImageId": "img-8toqc6s3",
                    "SystemDisk": {
                        "DiskSize": "50",
                        "DiskType": "CLOUD_BASIC"
                    },
                    "InternetAccessible": {
                        "PublicIpAssigned": "TRUE",
                        "InternetMaxBandwidthOut": "50"
                    },
                    "InstanceType": "S3.4XLARGE32",
                    "LoginSettings": {
                        "Password": "B1[habcd"
                    }
                }
            },
            {
                "EnvId": "env-lcpcej85",
                "EnvType": "MANAGED",
                "DesiredComputeNodeCount": 1,
                "EnvName": "batch-spot",
                "EnvDescription": "batch env ",
                "EnvData": {
                    "ImageId": "img-8toqc6s3",
                    "SystemDisk": {
                        "DiskSize": "50",
                        "DiskType": "CLOUD_BASIC"
                    },
                    "InternetAccessible": {
                        "PublicIpAssigned": "TRUE",
                        "InternetMaxBandwidthOut": "50"
                    },
                    "InstanceType": "S3.4XLARGE32",
                    "LoginSettings": {
                        "Password": "B1[habcd"
                    }
                }
            }
        ],
        "RequestId": "c50bfbf1-d214-4e41-90f6-39270dc9f071"
    }
}
```

