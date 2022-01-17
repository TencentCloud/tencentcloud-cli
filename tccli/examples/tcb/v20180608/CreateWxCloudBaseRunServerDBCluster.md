**Example 1: 开通微信云托管MySQL服务实例**

在微信云托管后台，用户开通MySQL时需要调用

Input: 

```
tccli tcb CreateWxCloudBaseRunServerDBCluster --cli-unfold-argument  \
    --EnvId xx \
    --AccountPassword xx \
    --DbVersion 5.7
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 2: success**



Input: 

```
tccli tcb CreateWxCloudBaseRunServerDBCluster --cli-unfold-argument  \
    --DbVersion 字符串 \
    --WxAppId 字符串 \
    --EnvId 字符串 \
    --AccountPassword 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "e1210cbf-f738-47f7-8e6d-2af814acece6"
    }
}
```

