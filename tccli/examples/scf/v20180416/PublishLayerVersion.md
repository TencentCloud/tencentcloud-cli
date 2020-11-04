**Example 1: 发布层版本**



Input: 

```
tccli scf PublishLayerVersion --cli-unfold-argument  \
    --LayerName <LayerName>\
    --CompatibleRuntimes <CompatibleRuntimes>\
    --Content <Content>\
    --Description <Description>\
    --LicenseInfo <LicenseInfo>
```

Output: 
```
{
    "Response": {
        "LayerVersion": 1
    }
}
```

