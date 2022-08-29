**Example 1: 关联APPID粒度的白名单公共服务**



Input: 

```
tccli vpc CreateOwnerWhiteServiceInternal --cli-unfold-argument  \
    --WhiteServiceRequestSet.0.Owner 123456 \
    --WhiteServiceRequestSet.0.WhiteServiceId 123 \
    --WhiteServiceRequestSet.0.AutoCompleteFlag 0 \
    --WhiteServiceRequestSet.0.CompleteOldFlag 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

