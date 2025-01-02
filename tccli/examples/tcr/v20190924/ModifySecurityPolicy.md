**Example 1: 更新实例外网白名单**



Input: 

```
tccli tcr ModifySecurityPolicy --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --PolicyIndex 2 \
    --CidrBlock 3.3.3.3 \
    --Description update access ip
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-dg284imq",
        "RequestId": "057c8440-07a9-4e00-a7cd-8be2372dfb90"
    }
}
```

