**Example 1: 开启主机自动扩容并选择旗舰版**

计费配置弹窗开启主机自动扩容并选择旗舰版

Input: 

```
tccli csip ModifyPayConfig --cli-unfold-argument  \
    --HostConfig.Switch ON \
    --HostConfig.ProtectType ULTIMATE
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

**Example 2: 关闭主机自动扩容**

计费配置弹窗关闭主机自动扩容

Input: 

```
tccli csip ModifyPayConfig --cli-unfold-argument  \
    --HostConfig.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "d479fbf3-9840-4dd3-c5f9-9f5395ba4c52"
    }
}
```

