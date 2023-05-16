**Example 1: 修改弹性网卡内网IP属性**

修改弹性网卡内网IP属性

Input: 

```
tccli vpc ModifyPrivateIpAddressesAttribute --cli-unfold-argument  \
    --NetworkInterfaceId eni-afo43z61 \
    --PrivateIpAddresses.0.PrivateIpAddress 172.16.32.111 \
    --PrivateIpAddresses.0.Description new-pip-name
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

