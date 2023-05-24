**Example 1: 删除SSL-VPN-SERVER**

删除SSL-VPN-SERVER

Input: 

```
tccli vpc DeleteVpnGatewaySslServer --cli-unfold-argument  \
    --SslVpnServerId vpns-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "aeabeab6-f74b-453a-b25d-d7b460193c3b",
        "TaskId": 123
    }
}
```

