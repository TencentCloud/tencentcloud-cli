**Example 1: Querying the configurations of cloud disks that are compatible with the S3 models in Guangzhou Zone 2**

This example shows you how to query the compatible configurations of cloud disks for a specified instance model. If the value of `Available` is `true` in the response, the cloud disk is available; if its value is `false`, the specified resources are sold out.

Input: 

```
tccli cbs DescribeDiskConfigQuota --cli-unfold-argument  \
    --InquiryType INQUIRY_CVM_CONFIG \
    --Zones ap-guangzhou-2 \
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

**Example 2: Querying the configurations of cloud disks in Guangzhou Zone 2**

This example shows you how to query the availability and configurations of cloud disks in an availability zone. If the value of `Available` is `true` in the response, there are available resources; if its value is `false`, the specified cloud disks are sold out.

Input: 

```
tccli cbs DescribeDiskConfigQuota --cli-unfold-argument  \
    --InquiryType INQUIRY_CBS_CONFIG \
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

