**Example 1: 修改用户SAML配置**

修改用户SAML配置

Input: 

```
tccli cam UpdateUserSAMLConfig --cli-unfold-argument  \
    --Operate updateSAML \
    --SAMLMetadataDocument metadataDocumentDemo
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

