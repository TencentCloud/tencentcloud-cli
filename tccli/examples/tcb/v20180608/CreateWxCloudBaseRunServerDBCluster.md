**Example 1: success**



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

**Example 2: success-20221010**



Input: 

```
tccli tcb CreateWxCloudBaseRunServerDBCluster --cli-unfold-argument  \
    --DbVersion 字符串 \
    --WxAppId 字符串 \
    --EnvId 字符串 \
    --LowerCaseTableName 字符串 \
    --AccountPassword 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "e1faa7da-a58b-44e1-9647-4782d8c11321"
    }
}
```

**Example 3: 开通微信云托管MySQL服务实例**

在微信云托管后台，用户开通MySQL时需要调用

Input: 

```
tccli tcb CreateWxCloudBaseRunServerDBCluster --cli-unfold-argument  \
    --EnvId env-test \
    --AccountPassword pwd-test \
    --DbVersion 5.7
```

Output: 
```
{
    "Response": {
        "RequestId": "asdasda-asfdafs"
    }
}
```

