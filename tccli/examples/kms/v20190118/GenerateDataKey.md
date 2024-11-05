**Example 1: 生成数据密钥示例**

使用指定的CMK生成Datakey。

Input: 

```
tccli kms GenerateDataKey --cli-unfold-argument  \
    --KeyId 93866e69-9755-11ef-8e65-52540089bc41 \
    --KeySpec AES_256 \
    --NumberOfBytes 32 \
    --EncryptionContext {"key1":"value1"} \
    --EncryptionPublicKey -----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoEcz****srLVydfJiHQuh2Jr9lMspgK58UVMJTvQCAU+Hztyhd6Aw==
-----END PUBLIC KEY----- \
    --EncryptionAlgorithm SM2
```

Output: 
```
{
    "Response": {
        "CiphertextBlob": "GPJUsGlmPcSjHKIktXGyzn33yestz+7NteW36M6FuL8hPfJ1xVfdO6Akr8sF69x3yBXMwto4njumJMIsi9WKow==-k-XqqalxTyNKIC1rITRePFGQ==-k-xAL9z9eXIHV/p+WT1RsHP3dm6f43bkomXjwmvWdMXH+JQoFORTThfXgcRh1f9lPNLENK4+fCOiQVG1VvLdA0RvcuRvU=",
        "KeyId": "93866e69-9755-11ef-8e65-52540089bc41",
        "Plaintext": "q+EouJ/tGeiZIo9/tIl2baxQOBFxcN0PNn7F6EIEvpDR6kvQmHohD5PTbUCKPkct6K8jOiYpbuaWZthxco0phMRSE4+HpB17rX4jmlW8pw3eHWOZo8yRyq/c7RVVo0+DtZofszwhMirQyjcBTJWhLt7xywtE5zqhDjngeEktAEw=",
        "RequestId": "044e823a-7a0c-4603-b03c-e99be5df998d"
    }
}
```

