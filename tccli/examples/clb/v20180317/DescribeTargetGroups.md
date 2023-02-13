**Example 1: 根据ID查询目标组信息**

根据ID查询目标组信息

Input: 

```
tccli clb DescribeTargetGroups --cli-unfold-argument  \
    --TargetGroupIds lbtg-5xunivs0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "6a932437-5ce7-4c30-a4ce-7076ef654dcd",
        "TargetGroupSet": [
            {
                "UpdatedTime": "2020-09-22 00:00:00",
                "TargetGroupId": "lbtg-xxxxxxxx",
                "VpcId": "vpc-xxxxxxxx",
                "CreatedTime": "2020-09-22 00:00:00",
                "AssociatedRule": [
                    {
                        "Domain": "www.xxxx.com",
                        "Protocol": "TCP",
                        "Url": "/xxxx",
                        "LoadBalancerName": "test_xxx",
                        "ListenerId": "lbl-xxxxxxxx",
                        "LocationId": "loc-xxxxxxxx",
                        "ListenerName": "test_xxx",
                        "LoadBalancerId": "lb-xxxxxxxx",
                        "Port": 80
                    },
                    {
                        "Domain": "www.xxxx.com",
                        "Protocol": "TCP",
                        "Url": "/xxxx",
                        "LoadBalancerName": "test_xxx",
                        "ListenerId": "lbl-xxxxxxxx",
                        "LocationId": "loc-xxxxxxxx",
                        "ListenerName": "test_xxx",
                        "LoadBalancerId": "lb-xxxxxxxx",
                        "Port": 801
                    }
                ],
                "Port": 1,
                "TargetGroupName": "test_xxxx"
            }
        ]
    }
}
```

**Example 2: 根据条件查询目标组信息**

根据条件查询目标组信息

Input: 

```
tccli clb DescribeTargetGroups --cli-unfold-argument  \
    --Filters.0.Values vpc-i1cnjuhx \
    --Filters.0.Name TargetGroupVpcId
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "TargetGroupSet": [
            {
                "TargetGroupId": "lbtg-5xunivs0",
                "VpcId": "vpc-i1cnjuhx",
                "TargetGroupName": "tg111_for_l4",
                "Port": 111,
                "CreatedTime": "2019-07-14 16:18:43",
                "UpdatedTime": "2019-07-14 16:18:43",
                "AssociatedRule": [
                    {
                        "LocationId": "loc-jjqr0ric",
                        "Domain": "aaaa.com",
                        "Url": "/",
                        "ListenerId": "lbl-m2q6sp9m",
                        "Port": 80,
                        "Protocol": "http",
                        "LoadBalancerId": "lb-phbx2420",
                        "LoadBalancerName": "lb-12f60e5",
                        "ListenerName": "aaa"
                    },
                    {
                        "LocationId": null,
                        "Domain": null,
                        "Url": null,
                        "ListenerId": "lbl-ow27ut6y",
                        "Port": 777,
                        "Protocol": "tcp",
                        "LoadBalancerId": "lb-phbx2420",
                        "LoadBalancerName": "lb-12f60e5",
                        "ListenerName": "asdfsdf"
                    }
                ]
            },
            {
                "TargetGroupId": "lbtg-dxnp10nc",
                "VpcId": "vpc-i1cnjuhx",
                "TargetGroupName": "tg111_for_l41563508267",
                "Port": 111,
                "CreatedTime": "2019-07-19 11:51:08",
                "UpdatedTime": "2019-07-19 11:51:07",
                "AssociatedRule": []
            },
            {
                "TargetGroupId": "lbtg-bjfi6nt6",
                "VpcId": "vpc-i1cnjuhx",
                "TargetGroupName": "tg111_for_l41563508507",
                "Port": 111,
                "CreatedTime": "2019-07-19 11:55:08",
                "UpdatedTime": "2019-07-19 11:55:08",
                "AssociatedRule": []
            }
        ],
        "RequestId": "412c7de5-47f6-4153-bf1b-77ef37e15244"
    }
}
```

