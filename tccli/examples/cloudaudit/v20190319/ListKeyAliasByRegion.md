**Example 1: 根据地域获取KMS密钥别名**

根据地域获取KMS密钥别名

Input: 

```
tccli cloudaudit ListKeyAliasByRegion --cli-unfold-argument  \
    --KmsRegion ap-hongkong \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00",
        "KeyMetadatas": [
            {
                "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01",
                "Alias": "KMS-CA"
            }
        ],
        "TotalCount": 1
    }
}
```

