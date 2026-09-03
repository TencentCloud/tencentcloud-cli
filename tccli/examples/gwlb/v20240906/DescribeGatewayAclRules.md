**Example 1: 查询网关负载均衡ACL规则**

查询网关负载均衡ACL规则

Input: 

```
tccli gwlb DescribeGatewayAclRules --cli-unfold-argument  \
    --AclGroupId gwlbacl-0pii****
```

Output: 
```
{
    "Response": {
        "GatewayAclRuleSet": [
            {
                "AclRuleId": "1024",
                "Priority": 1,
                "Type": "all",
                "VpcId": "all",
                "Action": "drop",
                "SrcIp": "10.0.0.0",
                "DstIp": "0.0.0.0",
                "SrcPort": 0,
                "DstPort": 0,
                "Protocol": "tcp",
                "CreateTime": "2023-05-22 14:36:48"
            },
            {
                "AclRuleId": "1025",
                "Priority": 2,
                "Type": "all",
                "VpcId": "vpc-b5oj****",
                "Action": "bypass",
                "SrcIp": "10.0.0.0",
                "DstIp": "1.1.1.1",
                "SrcPort": 80,
                "DstPort": 80,
                "Protocol": "all",
                "CreateTime": "2023-05-22 14:36:48"
            },
            {
                "AclRuleId": "",
                "Priority": -1,
                "Type": "in",
                "VpcId": "vpc-b5oj****",
                "Action": "drop",
                "SrcIp": "10.0.0.0",
                "DstIp": null,
                "SrcPort": null,
                "DstPort": null,
                "Protocol": null,
                "CreateTime": "2023-05-22 14:36:48"
            },
            {
                "AclRuleId": "",
                "Priority": -1,
                "Type": "out",
                "VpcId": "vpc-b5oj****",
                "Action": "bypass",
                "SrcIp": null,
                "DstIp": "10.0.0.0",
                "SrcPort": null,
                "DstPort": null,
                "Protocol": null,
                "CreateTime": "2023-05-22 14:36:48"
            }
        ],
        "RequestId": "6f5bed47-97b6-4f36-81bf-7862c1a9ad40",
        "TotalCount": 4
    }
}
```

