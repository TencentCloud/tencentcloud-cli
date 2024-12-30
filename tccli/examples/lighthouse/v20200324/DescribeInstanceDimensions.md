**Example 1: 获取一批实例的维度数据**

获取一批实例的维度数据。

Input: 

```
tccli lighthouse DescribeInstanceDimensions --cli-unfold-argument  \
    --Limit 10 \
    --NextToken M==
```

Output: 
```
{
    "Response": {
        "RequestId": "12cf1a6b-e64a-4a84-b525-f342e6ec4878",
        "InstanceDimensionsSet": [
            {
                "AppId": "1300257518",
                "Uin": "700000951429",
                "SubAccountUin": "700000951429",
                "InstanceId": "lhins-9usmvemx",
                "OriginInstanceId": "ins-a35yeyrk",
                "InstanceName": "Debian-ptYl",
                "InstanceType": "S1.MEDIUM2",
                "OsName": "Debian 10.2 64bit",
                "Platform": "DEBIAN",
                "PlatformType": "LINUX_UNIX",
                "InstanceChargeType": "PREPAID",
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": "60",
                "PrivateIpAddress": "10.0.16.10",
                "PublicIpAddress": "1.1.1.1",
                "PrivateIpv6Address": "",
                "PublicIpv6Address": "",
                "InternetMaxBandwidthOut": "3",
                "Zone": "ap-guangzhou-2",
                "InstanceState": "RUNNING",
                "Uuid": "588d02ff-7bcf-4f34-9531-72f3e6c74654"
            }
        ],
        "NextToken": "NDc0",
        "TotalCount": 7
    }
}
```

