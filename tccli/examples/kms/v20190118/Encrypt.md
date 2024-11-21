**Example 1: 加密接口示例**

使用CMK对小于4KB的数据加密。

Input: 

```
tccli kms Encrypt --cli-unfold-argument  \
    --KeyId 93866e69-9755-11ef-8e65-52540089bc41 \
    --Plaintext dGVzdAo= \
    --EncryptionContext {"key1":"value1"}
```

Output: 
```
{
    "Response": {
        "CiphertextBlob": "GPJUsGlmPcSjHKIktXGyzn33yestz+7NteW36M6FuL8hPfJ1xVfdO6Akr8sF69x3yBXMwto4njumJMIsi9WKow==-k-XqqalxTyNKIC1rITRePFGQ==-k-GqsANzNxvjjXhKwJAOY85vxYYm/2RtsCXRq7Q1iWbCAoeAtZ",
        "KeyId": "93866e69-9755-11ef-8e65-52540089bc41",
        "RequestId": "017f4b2a-4ae8-4d2c-a0d2-ec15e07d3deb"
    }
}
```

