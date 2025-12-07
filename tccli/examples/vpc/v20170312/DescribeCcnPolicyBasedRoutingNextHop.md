**Example 1: DescribeCcnPolicyBasedRoutingNextHop**



Input: 

```
tccli vpc DescribeCcnPolicyBasedRoutingNextHop --cli-unfold-argument  \
    --CcnId ccn-7bw2xi31
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "CcnPolicyBasedRoutingNextHopSet": [
            {
                "PolicyBasedRoutingNextHopId": "pbrnh-17zeoebp",
                "Name": "test2222",
                "NextHopRegion": "ap-guangzhou",
                "InstanceType": "VPC",
                "InstanceId": "vpc-hj0u9uv7",
                "NextHopResourceType": "HAVIP",
                "NextHopResourceId": "havip-lmojafue",
                "NextHopIp": "192.168.0.7",
                "Zone": "NONE",
                "State": "ENABLE",
                "Description": ""
            }
        ],
        "RequestId": "8caaae43-c96c-4d07-8964-6f4831a7328f"
    }
}
```

