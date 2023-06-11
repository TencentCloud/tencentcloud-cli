**Example 1: 查询网关负载均衡ACL规则**

查询网关负载均衡ACL规则

Input: 

```
tccli clb DescribeGatewayAclRules --cli-unfold-argument  \
    --AclGroupId gwlbacl-0pii****
```

Output: 
```
{
    "Response": {
        "GatewayAclRuleSet": [
            {
                "Action": "drop",
                "CreateTime": "2023-05-22 14:36:48",
                "DstIp": "0.0.0.0",
                "DstPort": 0,
                "Protocol": "tcp",
                "SrcIp": "10.0.0.0",
                "SrcPort": 0,
                "Type": "all",
                "VpcId": "all"
            },
            {
                "Action": "bypass",
                "CreateTime": "2023-05-22 14:36:48",
                "DstIp": "1.1.1.1",
                "DstPort": 80,
                "Protocol": "all",
                "SrcIp": "10.0.0.0",
                "SrcPort": 80,
                "Type": "all",
                "VpcId": "vpc-b5oj****"
            },
            {
                "Action": "drop",
                "CreateTime": "2023-05-22 14:36:48",
                "DstIp": null,
                "DstPort": null,
                "Protocol": null,
                "SrcIp": "10.0.0.0",
                "SrcPort": null,
                "Type": "in",
                "VpcId": "vpc-b5o*****"
            },
            {
                "Action": "bypass",
                "CreateTime": "2023-05-22 14:36:48",
                "DstIp": "10.0.0.0",
                "DstPort": null,
                "Protocol": null,
                "SrcIp": null,
                "SrcPort": null,
                "Type": "out",
                "VpcId": "vpc-b5o****"
            }
        ],
        "RequestId": "6f5bed47-97b6-4f36-81bf-7862c1a9ad40",
        "TotalCount": 4
    }
}
```

