**Example 1: Returning the private IPs of an ENI**



Input: 

```
tccli vpc UnassignPrivateIpAddresses --cli-unfold-argument  \
    --Version 2017-03-12 \
    --NetworkInterfaceId eni-afo43z61 \
    --PrivateIpAddresses.0.PrivateIpAddress 172.16.32.111
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

