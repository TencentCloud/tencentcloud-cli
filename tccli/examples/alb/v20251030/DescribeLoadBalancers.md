**Example 1: 查询负载均衡实例列表**



Input: 

```
tccli alb DescribeLoadBalancers --cli-unfold-argument  \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "LoadBalancers": [
            {
                "AddressIpVersion": "IPv4",
                "AddressType": "Internet",
                "CreateTime": "2026-05-25 18:27:42",
                "DeletionProtection": {
                    "DeletionProtectionEnabled": false,
                    "Reason": ""
                },
                "Domain": "alb-f8q2xk9m-c0rpri8t217fy3ii.gz-tencentalb.com",
                "LoadBalancerBillingConfig": {
                    "BandwidthPackageId": "bwp-q8m2x4pa",
                    "ChargeType": "POSTPAID_BY_HOUR"
                },
                "LoadBalancerId": "alb-f8q2xk9m",
                "LoadBalancerName": "alb-f8q2xk9m",
                "LoadBalancerOperationLocks": [],
                "LoadBalancerStatus": "Active",
                "ModificationProtection": {
                    "ModificationProtectionEnabled": false,
                    "OperatorUin": "",
                    "Reason": ""
                },
                "Tags": [],
                "VpcId": "vpc-92hffaxb"
            }
        ],
        "MaxResults": 1,
        "NextToken": "eyJsYXN0X3Jlc291cmNlX2lkIjogImFsYi01cWw0MHZzayIsICJsYXN0X2RiX2lkIjogNjY1MCwgInRvdGFsX2NvdW50IjogMjd9",
        "TotalCount": 27,
        "RequestId": "d635fb06-fa8a-41fe-bb34-ef1b0615364f"
    }
}
```

