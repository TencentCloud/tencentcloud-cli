**Example 1: 更新硬件信息**

更新硬件信息

Input: 

```
tccli mna UpdateHardware --cli-unfold-argument  \
    --HardwareId cpe-6zmf86knqu \
    --SN adsqda \
    --Description 描述
```

Output: 
```
{
    "Response": {
        "RequestId": "4ff707e0-c87a-6cff-5c65-93f21e212a81"
    }
}
```

**Example 2: 示例**

示例

Input: 

```
tccli mna UpdateHardware --cli-unfold-argument  \
    --HardwareId cpe-53g4emz6zc \
    --SN dd
```

Output: 
```
{
    "Response": {
        "RequestId": "004fa540-6023-46a1-8f92-bcf24d74e24f"
    }
}
```

