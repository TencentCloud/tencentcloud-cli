**Example 1: 创建智能语音模块**



Input: 

```
tccli ecm CreateModule --cli-unfold-argument  \
    --ModuleName 智能语音模块 \
    --DefaultBandWidth 50 \
    --DefaultImageId img-1tyt4apn \
    --InstanceType SN3ne.2XLARGE16 \
    --DefaultSystemDiskSize 50 \
    --DefaultDataDiskSize 100
```

Output: 
```
{
    "Response": {
        "RequestId": "418150c2-ff9e-409c-a6b3-c1a59d4775e3",
        "ModuleId": "em-r8nkc81r"
    }
}
```

