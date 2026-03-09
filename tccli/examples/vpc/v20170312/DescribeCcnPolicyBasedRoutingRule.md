**Example 1: DescribeCcnPolicyBasedRoutingRule**



Input: 

```
tccli vpc DescribeCcnPolicyBasedRoutingRule --cli-unfold-argument  \
    --CcnId ccn-7bw2xi31
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "CcnPolicyBasedRoutingRuleSet": [
            {
                "PolicyBasedRoutingRuleId": "pbrrule-mtptovl2",
                "PolicyBasedRoutingNextHopId": "pbrnh-rikj0itp",
                "InstanceType": "VPC",
                "InstanceId": "vpc-hj0u9uv7",
                "SourceCidrBlock": "10.0.0.0/16",
                "DestinationCidrBlock": "192.168.0.0/16",
                "Priority": 1,
                "Description": "pbr-1"
            }
        ],
        "RequestId": "226bff7f-89b7-4c8d-8d04-fa6e607e60d8"
    }
}
```

