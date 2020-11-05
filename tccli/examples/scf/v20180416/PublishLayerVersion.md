**Example 1: Publishing layer version**



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

