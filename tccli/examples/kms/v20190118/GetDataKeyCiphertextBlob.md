**Example 1: 下载数据密钥密文示例**

下载数据密钥密文

Input: 

```
tccli kms GetDataKeyCiphertextBlob --cli-unfold-argument  \
    --DataKeyId cb0f16e6-4f49-11f0-b672-52540073b995
```

Output: 
```
{
    "Response": {
        "CiphertextBlob": "KoFmB5Ro70M6wfNJe1xlzriwwyn4Ypj6cjXNUbhbEE7+cAtl4ym/EIj3aAzK0Sa6GKgPzyor+zC7bUhRyB5eeQ==-k-fKVP3WIlGpg8m9LMW4jEkQ==-k-yMhT0yaoSueIApZePMxwBZ0y6EjfaKdxvvPhk9LT1ldmhb+Z",
        "RequestId": "88d9d828-f019-4625-b0f7-75b57dd2e582"
    }
}
```

