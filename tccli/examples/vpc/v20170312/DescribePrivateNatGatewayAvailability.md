**Example 1: 查询私网NAT是否售罄**



Input: 

```
tccli vpc DescribePrivateNatGatewayAvailability --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NatGatewayAvailabilitySet": [
            {
                "ResourceType": "PrivateNat",
                "Availability": "Unavailable"
            }
        ],
        "RequestId": "69de593c-bdff-4a4b-b923-1dfed70457a9"
    }
}
```

