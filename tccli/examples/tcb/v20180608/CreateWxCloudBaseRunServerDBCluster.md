**Example 1: 开通微信云托管MySQL服务实例**

在微信云托管后台，用户开通MySQL时需要调用

Input: 

```
tccli tcb CreateWxCloudBaseRunServerDBCluster --cli-unfold-argument  \
    --EnvId xx \
    --AccountPassword xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

