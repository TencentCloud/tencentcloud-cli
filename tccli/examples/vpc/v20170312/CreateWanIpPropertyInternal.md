**Example 1: 添加外网属性**



Input: 

```
tccli vpc CreateWanIpPropertyInternal --cli-unfold-argument  \
    --AddWanIpPropertySet.0.WanIp 1.1.1.1 \
    --AddWanIpPropertySet.0.VpcId 1 \
    --AddWanIpPropertySet.0.Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

