**Example 1: 申请互联网BGP IPv4地址**



Input: 

```
tccli dc ApplyInternetAddress --cli-unfold-argument  \
    --AddrType 0 \
    --AddrProto 0 \
    --MaskLen 30
```

Output: 
```
{
    "Response": {
        "InstanceId": "ipv4-h2k2jna1",
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

