**Example 1: Querying target group information by ID**



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
            }
        ],
        "RequestId": "53f129a5-0ab5-4514-a629-f4c33af11892"
    }
}
```

**Example 2: Querying target group information by filter**



Input: 

```
tccli clb DescribeTargetGroups --cli-unfold-argument  \
    --Filters.0.Name TargetGroupVpcId\
    --Filters.0.Values vpc-i1cnjuhx
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

