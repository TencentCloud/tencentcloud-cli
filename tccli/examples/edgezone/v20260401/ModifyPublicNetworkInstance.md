**Example 1: 修改公网实例名称**



Input: 

```
tccli edgezone ModifyPublicNetworkInstance --cli-unfold-argument  \
    --NetworkInstanceId epn-dfghjkl1 \
    --NetworkInstanceName 新实例名称
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-004"
    }
}
```

