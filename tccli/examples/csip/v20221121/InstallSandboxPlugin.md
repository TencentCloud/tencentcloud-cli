**Example 1: 对指定主机下发流量沙箱插件安装任务**



Input: 

```
tccli csip InstallSandboxPlugin --cli-unfold-argument  \
    --BelongAssetType HOST \
    --EffectScope.EffectType INCLUDE \
    --EffectScope.EffectAssets.0.InstanceId ins-a1b2c3d4
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

