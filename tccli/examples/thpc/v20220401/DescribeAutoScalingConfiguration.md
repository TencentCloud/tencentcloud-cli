**Example 1: 查询扩缩容策略配置**

查询集群ID为hpc-rv7hahw2的集群弹性伸缩配置信息。

Input: 

```
tccli thpc DescribeAutoScalingConfiguration --cli-unfold-argument  \
    --ClusterId hpc-rv7hahw2
```

Output: 
```
{
    "Response": {
        "ClusterId": "hpc-rv7hahw2",
        "ExpansionBusyTime": 120,
        "ShrinkIdleTime": 300,
        "QueueConfigs": [
            {
                "QueueName": "compute",
                "MinSize": 0,
                "MaxSize": 10,
                "EnableAutoExpansion": false,
                "EnableAutoShrink": false,
                "ExpansionNodeConfigs": [
                    {
                        "InstanceType": "M5.SMALL8",
                        "Placement": {
                            "Zone": "ap-chongqing-1"
                        },
                        "InstanceChargeType": "POSTPAID_BY_HOUR",
                        "InstanceChargePrepaid": null,
                        "VirtualPrivateCloud": {
                            "VpcId": "vpc-r9jw2jzv",
                            "SubnetId": "subnet-r0zpktae"
                        },
                        "ImageId": "img-l8og963d",
                        "InternetAccessible": {
                            "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                            "InternetMaxBandwidthOut": 0
                        },
                        "SystemDisk": {
                            "DiskType": "CLOUD_BSSD",
                            "DiskSize": 50
                        },
                        "DataDisks": null
                    }
                ]
            }
        ],
        "RequestId": "935760b6-2a63-480d-9124-c5f5b9d4218b"
    }
}
```

