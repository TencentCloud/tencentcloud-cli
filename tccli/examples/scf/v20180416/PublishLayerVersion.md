**Example 1: 发布层版本**

发布层版本

Input: 

```
tccli scf PublishLayerVersion --cli-unfold-argument  \
    --LayerName layer-name1 \
    --CompatibleRuntimes Nodejs16.13 \
    --Content.CosBucketName layer-name1-2343243543 \
    --Content.CosObjectName layer-name1/node_modules.zip \
    --Content.CosBucketRegion ap-singapore \
    --Description a layer
```

Output: 
```
{
    "Response": {
        "LayerVersion": 8,
        "RequestId": "197192d3-0b64-410a-8cd9-25cb7c1db0ee"
    }
}
```

