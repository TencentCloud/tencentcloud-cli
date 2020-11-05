**Example 1: Applies for private IPs for an ENI**



Input: 

```
tccli vpc AssignPrivateIpAddresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-afo43z61\
    --SecondaryPrivateIpAddressCount 2
```

Output: 
```
{
    "Response": {
        "PrivateIpAddressSet": [
            {
                "PrivateIpAddress": "172.16.32.237"
            },
            {
                "PrivateIpAddress": "172.16.32.84"
            }
        ],
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

