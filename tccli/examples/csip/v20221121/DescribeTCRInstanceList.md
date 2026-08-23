**Example 1: 获取TCR实例列表**



Input: 

```
tccli csip DescribeTCRInstanceList --cli-unfold-argument  \
    --AccessKey AKID******************************** \
    --SecretKey c5Owz*************************** \
    --MemberId mem-12e1se11 \
    --RegistryRegion ap-guangzhou \
    --RegistryId 5
```

Output: 
```
{
    "Response": {
        "Registries": [
            {
                "PublicDomain": "s*******.tencentcloudcr.com",
                "RegistryId": "tcr-7*******",
                "RegistryName": "s*******",
                "RegistryRegion": "ap-guangzhou",
                "RegistryRegionId": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "ebcaba23-3c9c-484e-8868-64fa65dbf717"
    }
}
```

