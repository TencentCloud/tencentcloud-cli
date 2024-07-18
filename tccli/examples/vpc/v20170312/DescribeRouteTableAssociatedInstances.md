**Example 1: 查询路由表绑定实例列表**

查询路由表绑定实例列表

Input: 

```
tccli vpc DescribeRouteTableAssociatedInstances --cli-unfold-argument  \
    --Filters.0.Name route-table-id \
    --Filters.0.Values ccnrtb-mnvhfmv9 ccnrtb-3230jx4x \
    --Filters.1.Name instance-type \
    --Filters.1.Values VPC \
    --Filters.2.Name ccn-id \
    --Filters.2.Values ccn-8j0phqix \
    --Filters.3.Name instance-id \
    --Filters.3.Values vpc-q2nxods9
```

Output: 
```
{
    "Response": {
        "InstanceBindSet": [
            {
                "CcnId": "ccn-8j0phqix",
                "InstanceType": "VPC",
                "InstanceId": "vpc-q2nxods9",
                "InstanceBindTime": "2021-05-20 16:39:34",
                "RouteTableId": "ccnrtb-3230jx4x",
                "InstanceName": "rubytest",
                "State": "0",
                "InstanceRegion": [
                    "ap-guangzhou"
                ],
                "InstanceUin": "329087131"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ad8d1a59-fd88-4e47-b3ab-79c97efa7b5e"
    }
}
```

