**Example 1: 获取资源详情**

获取资源详情

Input: 

```
tccli config DescribeDiscoveredResource --cli-unfold-argument  \
    --ResourceId ins-2avl1cxx \
    --ResourceType QCS::CVM::Instance \
    --ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "2ea2d804-d278-4631-b04d-70bd40e1a478",
        "Configuration": "{\"InstanceState\":\"RUNNING\",\"InstanceName\":\"未命名\",\"InstanceId\":\"ins-111\",\"InstanceType\":\"S5.SMALL2\",\"VirtualPrivateCloud\":{\"VpcId\":\"vpc-333\",\"SubnetId\":\"subnet-qxupkefw\",\"AsVpcGateway\":false,\"PrivateIpAddresses\":null,\"Ipv6AddressCount\":0},\"PrivateIpAddresses\":[\"111\"],\"PublicIpAddresses\":null,\"OsName\":\"TencentOS Server 4 for x86_64\",\"Memory\":2,\"CPU\":1,\"InternetAccessible\":{\"InternetChargeType\":\"\",\"InternetMaxBandwidthOut\":0,\"PublicIpAssigned\":false,\"BandwidthPackageId\":\"\"},\"ImageId\":\"img-333\",\"InstanceChargeType\":\"PREPAID\",\"SecurityGroupIds\":[\"sg-222\"],\"DataDisks\":null,\"SystemDisk\":{\"DiskType\":\"CLOUD_PREMIUM\",\"DiskId\":\"disk-auh4557w\"},\"ExpiredTime\":\"2024-12-28T08:07:12Z\",\"RenewFlag\":\"NOTIFY_AND_MANUAL_RENEW\",\"LatestOperation\":\"\",\"Placement\":{\"ProjectId\":0},\"LatestOperationState\":\"\",\"CamRoleName\":\"\"}",
        "ResourceCreateTime": "2024-11-28 16:07:12",
        "ResourceId": "ins-2avl1cxx",
        "ResourceName": "未命名",
        "ResourceRegion": "ap-guangzhou",
        "ResourceType": "QCS::CVM::Instance",
        "ResourceZone": "",
        "Tags": [],
        "UpdateTime": "2024-11-28 16:08:36"
    }
}
```

