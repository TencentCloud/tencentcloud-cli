**Example 1: 修改IPV6地址带宽**



Input: 

```
tccli ecm ModifyIpv6AddressesBandwidth --cli-unfold-argument  \
    --EcmRegion ap-guangzhou-ecm-cu2 \
    --Ipv6Addresses.0.Address 2402:4e00:1000:200:0:8d8a:60b7:87f8 \
    --InternetMaxBandwidthOut 50
```

Output: 
```
{
    "Response": {
        "RequestId": "61b49567-8cbf-4523-8f25-7a2c9da23ddb"
    }
}
```

