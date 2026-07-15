**Example 1: 创建公网实例**



Input: 

```
tccli edgezone CreatePublicNetworkInstance --cli-unfold-argument  \
    --ZoneId ap-beijing-a \
    --NetworkInstanceName test-bgp-instance \
    --Line BGP \
    --Bandwidth 100 \
    --RouteMode bgp
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-001",
        "NetworkInstanceId": "epn-a1b2c3d4"
    }
}
```

