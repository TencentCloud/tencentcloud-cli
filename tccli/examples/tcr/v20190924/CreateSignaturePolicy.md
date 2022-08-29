**Example 1: 创建镜像加签策略**



Input: 

```
tccli tcr CreateSignaturePolicy --cli-unfold-argument  \
    --RegistryId tcr-f7g1ir99 \
    --Name library 加签 \
    --NamespaceName library \
    --KmsId 08408a30-0416-11ed-abdc-52540036b432 \
    --KmsRegion  \
    --Disabled False
```

Output: 
```
{
    "Response": {
        "RequestId": "866bda78-ed75-4b10-8876-e82de555f69b"
    }
}
```

