**Example 1: 创建缓存卷**

创建缓存卷。

Input: 

```
tccli omics CreateVolume --cli-unfold-argument  \
    --EnvironmentId menv-ry46eloh \
    --Name 测试缓存就 \
    --Type SHARED \
    --Spec HP \
    --Capacity 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d79c957c-adca-4e29-81ba-1add68284e09",
        "VolumeId": "vol-mpcb5xnl"
    }
}
```

