**Example 1: 查询HPC节点列表**

查询HPC节点列表。

Input: 

```
tccli omics DescribeHPCNodes --cli-unfold-argument  \
    --ClusterId hpc-an7qz1jg
```

Output: 
```
{
    "Response": {
        "Nodes": [
            {
                "ClusterId": "hpc-an7qz1jg",
                "ImageId": "img-l8og963d",
                "Instance": {
                    "CPU": 2,
                    "ChargeType": "POSTPAID_BY_HOUR",
                    "CreateTime": "2024-07-09T16:53:15+08:00",
                    "ExpireTime": "2024-08-09T16:53:15+08:00",
                    "InstanceId": "ins-hsjwv87a",
                    "Memory": 4,
                    "Name": "未命名",
                    "OSName": "CentOS 7.9 64位",
                    "PrivateIPAddresses": [
                        "10.1.0.91"
                    ],
                    "PublicIPAddresses": [],
                    "State": "RUNNING",
                    "SystemDisk": {
                        "DiskId": "disk-hajjdzfu",
                        "Size": 50,
                        "Type": "CLOUD_PREMIUM"
                    },
                    "Type": "SA2.MEDIUM4"
                },
                "NodeId": "node-exg8nn7f",
                "QueueId": "",
                "Role": "MANAGER",
                "Tags": [],
                "Type": "STATIC",
                "Zone": "ap-guangzhou-6"
            },
            {
                "ClusterId": "hpc-an7qz1jg",
                "ImageId": "img-l8og963d",
                "Instance": {
                    "CPU": 2,
                    "ChargeType": "POSTPAID_BY_HOUR",
                    "CreateTime": "2024-07-09T16:52:46+08:00",
                    "ExpireTime": "2024-08-09T16:52:46+08:00",
                    "InstanceId": "ins-hwifb6n8",
                    "Memory": 4,
                    "Name": "未命名",
                    "OSName": "CentOS 7.9 64位",
                    "PrivateIPAddresses": [
                        "10.1.8.62"
                    ],
                    "PublicIPAddresses": [
                        "106.53.59.92"
                    ],
                    "State": "RUNNING",
                    "SystemDisk": {
                        "DiskId": "disk-dvfroio2",
                        "Size": 50,
                        "Type": "CLOUD_PREMIUM"
                    },
                    "Type": "SA2.MEDIUM4"
                },
                "NodeId": "node-ifrzwo4f",
                "QueueId": "queue-dq1spf9m",
                "Role": "COMPUTE",
                "Tags": [],
                "Type": "DYNAMIC",
                "Zone": "ap-guangzhou-6"
            },
            {
                "ClusterId": "hpc-an7qz1jg",
                "ImageId": "img-l8og963d",
                "Instance": {
                    "CPU": 4,
                    "ChargeType": "POSTPAID_BY_HOUR",
                    "CreateTime": "2024-07-16T18:14:07+08:00",
                    "ExpireTime": "2024-08-09T16:52:46+08:00",
                    "InstanceId": "ins-8rrp4n6s",
                    "Memory": 8,
                    "Name": "未命名",
                    "OSName": "CentOS 7.9 64位",
                    "PrivateIPAddresses": [
                        "10.1.3.200"
                    ],
                    "PublicIPAddresses": [],
                    "State": "RUNNING",
                    "SystemDisk": {
                        "DiskId": "disk-ofrnd2a4",
                        "Size": 50,
                        "Type": "CLOUD_PREMIUM"
                    },
                    "Type": "SA2.LARGE8"
                },
                "NodeId": "node-cqjk6pbz",
                "QueueId": "queue-dq1spf9m",
                "Role": "COMPUTE",
                "Tags": [],
                "Type": "STATIC",
                "Zone": "ap-guangzhou-6"
            }
        ],
        "RequestId": "1ab0bd99-190f-4419-b048-8bf798164944",
        "TotalCount": 3
    }
}
```

