**Example 1: 申请互联网BGP IPv4地址**



Input: 

```
tccli dc ApplyInternetAddress --cli-unfold-argument  \
    --AddrType 0 \
    --MaskLen 30 \
    --AddrProto 0
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

**Example 2: 远程出口公网IP申请示例**



Input: 

```
tccli dc ApplyInternetAddress --cli-unfold-argument  \
    --AddrType 1 \
    --MaskLen 30 \
    --AddrProto 0
```

Output: 
```
{
    "Response": {
        "InstanceId": "ipv4-ljm17pbl",
        "RequestId": "4a871804-9877-43f3-a2ba-0c213ab72af9"
    }
}
```

