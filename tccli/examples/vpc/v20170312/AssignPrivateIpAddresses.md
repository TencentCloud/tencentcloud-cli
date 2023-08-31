**Example 1: 弹性网卡申请内网 IP**

申请弹性网卡

Input: 

```
tccli vpc AssignPrivateIpAddresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-afo43z61 \
    --SecondaryPrivateIpAddressCount 1
```

Output: 
```
{
    "Response": {
        "PrivateIpAddressSet": [
            {
                "PrivateIpAddress": "172.16.32.237",
                "Primary": false,
                "PublicIpAddress": "",
                "AddressId": "",
                "Description": "",
                "IsWanIpBlocked": false,
                "State": "PENDING",
                "QosLevel": "DEFAULT"
            }
        ],
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

