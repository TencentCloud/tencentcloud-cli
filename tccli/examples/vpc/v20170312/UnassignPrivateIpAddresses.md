**Example 1: 弹性网卡退还内网 IP**

弹性网卡退还内网 IP

Input: 

```
tccli vpc UnassignPrivateIpAddresses --cli-unfold-argument  \
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

