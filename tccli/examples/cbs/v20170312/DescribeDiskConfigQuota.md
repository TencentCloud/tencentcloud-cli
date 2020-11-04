**Example 1: 查询广州二区的云硬盘配置**

查询各可用区云盘规格配置及售罄情况，返回结果中Available为true表示当前可购买，为false表示对应规格云盘已售罄。

Input: 

```
tccli cbs DescribeDiskConfigQuota --cli-unfold-argument  \
    --InquiryType INQUIRY_CBS_CONFIG\
    --Zones ap-guangzhou-2
```

Output: 
```
{
    "Response": {
        "DiskConfigSet": [
            {
                "Available": true,
                "DiskChargeType": "POSTPAID_BY_HOUR",
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": null,
                "DiskType": "CLOUD_BASIC",
                "DeviceClass": null,
                "DiskUsage": "DATA_DISK",
                "MinDiskSize": 10,
                "MaxDiskSize": 4000
            },
            {
                "Available": true,
                "DiskChargeType": "POSTPAID_BY_HOUR",
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": null,
                "DiskType": "CLOUD_PREMIUM",
                "DeviceClass": null,
                "DiskUsage": "DATA_DISK",
                "MinDiskSize": 50,
                "MaxDiskSize": 4000
            },
            {
                "Available": false,
                "DiskChargeType": "POSTPAID_BY_HOUR",
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": null,
                "DiskType": "CLOUD_SSD",
                "DeviceClass": null,
                "DiskUsage": "DATA_DISK",
                "MinDiskSize": 100,
                "MaxDiskSize": 4000
            }
        ],
        "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6814b2"
    }
}
```

**Example 2: 查询广州二区S3机型可搭配的云盘配置**

查询不同实例机型可搭配的云盘配置，返回结果中Available为true表示当前可购买，为false表示对应规格云盘已售罄。

Input: 

```
tccli cbs DescribeDiskConfigQuota --cli-unfold-argument  \
    --InquiryType INQUIRY_CVM_CONFIG\
    --Zones ap-guangzhou-2\
    --InstanceFamilies S3
```

Output: 
```
{
    "Response": {
        "DiskConfigSet": [
            {
                "Available": true,
                "MaxDiskSize": 16000,
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "S3",
                "DiskType": "CLOUD_BASIC",
                "DeviceClass": "VSELF_3",
                "DiskUsage": "DATA_DISK",
                "MinDiskSize": 10,
                "DiskChargeType": "POSTPAID_BY_HOUR"
            },
            {
                "Available": true,
                "MaxDiskSize": 500,
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "S3",
                "DiskType": "CLOUD_BASIC",
                "DeviceClass": "VSELF_3",
                "DiskUsage": "SYSTEM_DISK",
                "MinDiskSize": 50,
                "DiskChargeType": "POSTPAID_BY_HOUR"
            },
            {
                "Available": true,
                "MaxDiskSize": 16000,
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "S3",
                "DiskType": "CLOUD_SSD",
                "DeviceClass": "VSELF_3",
                "DiskUsage": "DATA_DISK",
                "MinDiskSize": 100,
                "DiskChargeType": "POSTPAID_BY_HOUR"
            },
            {
                "Available": true,
                "MaxDiskSize": 500,
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "S3",
                "DiskType": "CLOUD_SSD",
                "DeviceClass": "VSELF_3",
                "DiskUsage": "SYSTEM_DISK",
                "MinDiskSize": 50,
                "DiskChargeType": "POSTPAID_BY_HOUR"
            }
        ],
        "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6814b2"
    }
}
```

