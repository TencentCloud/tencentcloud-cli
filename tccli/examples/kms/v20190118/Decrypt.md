**Example 1: 解密接口示例**

用于对密文解密

Input: 

```
tccli kms Decrypt --cli-unfold-argument  \
    --CiphertextBlob GPJUsGlmPcSjHKIktXGyzn33yestz+7NteW36M6FuL8hPfJ1xVfdO6Akr8sF69x3yBXMwto4njumJMIsi9WKow==-k-XqqalxTyNKIC1rITRePFGQ==-k-GqsANzNxvjjXhKwJAOY85vxYYm/2RtsCXRq7Q1iWbCAoeAtZ \
    --EncryptionContext {"key1":"value1"} \
    --EncryptionAlgorithm SM2
```

Output: 
```
{
    "Response": {
        "KeyId": "93866e69-9755-11ef-8e65-52540089bc41",
        "Plaintext": "dGVzdAo=",
        "RequestId": "4c857b16-e977-4086-b33a-532613f03abd"
    }
}
```

