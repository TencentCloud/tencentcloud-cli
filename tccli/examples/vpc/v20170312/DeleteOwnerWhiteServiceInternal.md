**Example 1: 解除关联APPID粒度的白名单公共服务**



Input: 

```
tccli vpc DeleteOwnerWhiteServiceInternal --cli-unfold-argument  \
    --DeleteWhiteServiceRequestSet.0.Owner 123456 \
    --DeleteWhiteServiceRequestSet.0.WhiteServiceId vpc-xxxxxxxx \
    --DeleteWhiteServiceRequestSet.0.DelVpcWhiteServiceFlag 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

