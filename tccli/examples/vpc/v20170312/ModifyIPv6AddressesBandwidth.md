**Example 1: 批量调整弹性公网IPv6地址带宽**

批量调整弹性公网IPv6地址带宽。

Input: 

```
tccli vpc ModifyIPv6AddressesBandwidth --cli-unfold-argument  \
    --IPv6AddressIds eipv6-2ucdpy9t eipv6-3lxpc6sh \
    --InternetMaxBandwidthOut 20
```

Output: 
```
{
    "Response": {
        "RequestId": "a6661e38-e981-4369-af26-b6f1a7e21a1d"
    }
}
```

