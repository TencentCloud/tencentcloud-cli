**Example 1: 复制企业版仓库镜像版本**

复制企业版仓库镜像版本

Input: 

```
tccli tcr DuplicateImage --cli-unfold-argument  \
    --RegistryId tcr-e8pg46c6 \
    --SourceNamespace develop \
    --SourceRepo app \
    --SourceReference stg \
    --DestinationNamespace release \
    --DestinationRepo app \
    --DestinationTag prd \
    --Override True
```

Output: 
```
{
    "Response": {
        "RequestId": "eee33f6d-9271-4894-aaf6-14642d5a88da"
    }
}
```

