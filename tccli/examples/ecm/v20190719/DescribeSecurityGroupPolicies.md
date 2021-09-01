**Example 1: 查询安全组规则**



Input: 

```
tccli ecm DescribeSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId esg-ohuuioma
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b",
        "SecurityGroupPolicySet": {
            "Version": "1",
            "Egress": [
                {
                    "PolicyIndex": 1,
                    "Protocol": "tcp",
                    "Port": "80",
                    "ServiceTemplate": {
                        "ServiceId": "",
                        "ServiceGroupId": ""
                    },
                    "SecurityGroupId": "",
                    "CidrBlock": "20.0.0.0/16",
                    "Action": "ACCEPT",
                    "PolicyDescription": "test1",
                    "AddressTemplate": {
                        "AddressId": "",
                        "AddressGroupId": ""
                    }
                }
            ],
            "Ingress": [
                {
                    "PolicyIndex": 2,
                    "Protocol": "tcp",
                    "Port": "8080",
                    "CidrBlock": "10.0.0.0/16",
                    "ServiceTemplate": {
                        "ServiceId": "",
                        "ServiceGroupId": ""
                    },
                    "SecurityGroupId": "",
                    "Action": "ACCEPT",
                    "PolicyDescription": "test-2",
                    "AddressTemplate": {
                        "AddressId": "",
                        "AddressGroupId": ""
                    }
                }
            ]
        }
    }
}
```

