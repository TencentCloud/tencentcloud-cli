**Example 1: 查看网关负载均衡ACL组**

查看网关负载均衡ACL组

Input: 

```
tccli gwlb DescribeGatewayAclGroups --cli-unfold-argument  \
    --Filters.0.Name VpcId \
    --Filters.0.Values vpc-b50****
```

Output: 
```
{
    "Response": {
        "GatewayAclGroupSet": [
            {
                "AclGroupId": "gwlbacl-ryrl****",
                "AclGroupName": "gwlb-acl-group-prod",
                "AssociatedInstances": [
                    "gwlb-owlo****"
                ],
                "CreateTime": "2023-03-22 10:39:03",
                "VpcId": "vpc-b5oj****"
            }
        ],
        "RequestId": "6379bfea-3828-4e8c-b9dd-39079d628f5f",
        "TotalCount": 1
    }
}
```

