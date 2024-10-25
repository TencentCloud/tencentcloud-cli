**Example 1: 显示目标组绑定的服务器信息**

显示目标组绑定的服务器信息

Input: 

```
tccli gwlb DescribeTargetGroupInstances --cli-unfold-argument  \
    --Filters.0.Name TargetGroupId \
    --Filters.0.Values lbtg-5xunivs0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TargetGroupInstanceSet": [
            {
                "TargetGroupId": "lbtg-5xunivs0",
                "Type": "CVM",
                "InstanceId": "ins-197234qt",
                "InstanceName": "未命名",
                "Port": 3333,
                "Weight": 43,
                "PublicIpAddresses": [],
                "PrivateIpAddresses": [
                    "172.16.0.32"
                ],
                "EniId": null,
                "ZoneId": "400001",
                "RegisteredTime": "2019-07-24T20:02:43+08:00"
            },
            {
                "TargetGroupId": "lbtg-5xunivs0",
                "Type": "CVM",
                "InstanceId": "ins-197234qt",
                "InstanceName": "未命名",
                "Port": 2222,
                "Weight": 55,
                "PublicIpAddresses": [],
                "PrivateIpAddresses": [
                    "172.16.0.32"
                ],
                "EniId": null,
                "ZoneId": "400001",
                "RegisteredTime": "2019-07-23T21:01:08+08:00"
            }
        ],
        "RealCount": 2,
        "RequestId": "94240d7f-8bc1-422a-81b9-5ea76d486a66"
    }
}
```

