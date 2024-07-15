**Example 1: 查询路由选择策略**

查询路由选择策略

Input: 

```
tccli vpc DescribeRouteTableSelectionPolicies --cli-unfold-argument  \
    --Filters.0.Name ccn-id \
    --Filters.0.Values ccn-8j0phqix \
    --Filters.1.Name instance-id \
    --Filters.1.Values vpc-q2nxods9 \
    --Filters.2.Name ccn-route-table-id \
    --Filters.2.Values ccnrtb-b0v86f8t \
    --Filters.3.Name instance-type \
    --Filters.3.Values VPC
```

Output: 
```
{
    "Response": {
        "RouteSelectionPolicySet": [
            {
                "CcnId": "ccn-8j0phqix",
                "RouteTableId": "ccnrtb-b0v86f8t",
                "RouteTableName": "rubytest222",
                "Description": "ruby",
                "InstanceType": 0,
                "InstanceId": "vpc-q2nxods9",
                "InstanceUin": "329087131",
                "SourceCidrBlock": "10.0.0.0/24",
                "InstanceName": "rubytest"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6ed83da8-7eaf-48a4-8488-61bd9c710cfa"
    }
}
```

