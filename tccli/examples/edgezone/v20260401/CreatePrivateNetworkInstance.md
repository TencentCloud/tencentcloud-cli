**Example 1: 创建私网实例**



Input: 

```
tccli edgezone CreatePrivateNetworkInstance --cli-unfold-argument  \
    --NetworkInstanceName test-pri-instance \
    --ZoneId ap-beijing \
    --Network 10.0.0.0 \
    --Mask 24
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-011",
        "NetworkInstanceId": "ein-a1b2c3d4"
    }
}
```

