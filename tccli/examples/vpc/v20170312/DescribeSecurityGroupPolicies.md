**Example 1: 查询安全组规则**



Input: 

```
tccli vpc DescribeSecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12\
    --SecurityGroupId sg-ohuuioma
```

Output: 
```
{
    "Response": {
        "SecurityGroupPolicySet": {
            "Ingress": [
                {
                    "PolicyIndex": 0,
                    "Direction": "INGRESS",
                    "ServiceTemplate": {
                        "ServiceId": "ppm-f5n1f8da"
                    },
                    "AddressTemplate": {
                        "AddressGroupId": "ipmg-2uw6ujo6"
                    },
                    "Action": "ACCEPT",
                    "ModifyTime": "2017-03-12 10:00:00",
                    "PolicyDescription": "ModifyPolicies"
                },
                {
                    "PolicyIndex": 1,
                    "Direction": "INGRESS",
                    "ServiceTemplate": {
                        "ServiceId": "ppm-f5n1f8da"
                    },
                    "AddressTemplate": {
                        "AddressGroupId": "ipmg-2uw6ujo6"
                    },
                    "Action": "ACCEPT",
                    "ModifyTime": "2017-03-12 10:00:00",
                    "PolicyDescription": "2"
                }
            ],
            "Egress": [
                {
                    "PolicyIndex": 0,
                    "Direction": "EGRESS",
                    "ServiceTemplate": {
                        "ServiceId": "ppm-f5n1f8da"
                    },
                    "AddressTemplate": {
                        "AddressGroupId": "ipmg-2uw6ujo6"
                    },
                    "Action": "ACCEPT",
                    "ModifyTime": "2017-03-12 10:00:00",
                    "PolicyDescription": "E1"
                }
            ],
            "Version": 60
        },
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

