**Example 1: 身份证识别（安全加密版）示例**

身份证识别（安全加密版）示例

Input: 

```
tccli ocr RecognizeEncryptedIDCardOCR --cli-unfold-argument  \
    --ImageBase64  \
    --ImageUrl  \
    --CardSide  \
    --Config  \
    --EncryptedBody cpA8uWgtLjDSY8NvIoRe/UH0LlAa8+a3Jj6lVN5+9u4LFQxEj3x3QqNnPXZJ3f5aAcEYZPxnaglJVSzimWT8rDKJmnFRU2309cJysuV7GVZgfiLPlAtZ659BRUYTgZD2aLSSD2WJZt1izHmPx1Lt1A== \
    --Encryption.Algorithm AES-256-CBC \
    --Encryption.CiphertextBlob sBmIZTmfcZ4FZIskKB1PC3yYx0a/CxBh8KwnQWgsgK96UeHeswIJdH7Gt4LW8yiIUjFq7PdikshkRdYPk9OWWEfAWb70DjfNnWLhI8FMMT72A+V+uWeQZN4VtwWdH6I2FrV4aXYxblq7cHHALvL1Ey8x0Cl9CFBeIrQsBGNnnW8= \
    --Encryption.Iv U2KHDqXYtpCl3l5BRuH0qw== \
    --Encryption.EncryptList EncryptedBody
```

Output: 
```
{
    "Response": {
        "Address": "",
        "AdvancedInfo": "",
        "Authority": "",
        "Birth": "",
        "EncryptedBody": "R+psIR59D8HR23D2S1SpEDrR0GPkpzQ+ynmilaOGMI0b/qKNJVYxo/myjctCdswpctobCP+QDd1nG0tYe651VfkcgBYcRPjEKp7sXKIKsOL7f6kilHoLkCCbpzXGq+Q6c+A+TdxUC36xT8jfYF/5mFqRD/qnEqlg/9L/6SeJ+6TQ0CWPmlAzw2dRWvSHq/sigMd98CAsk9M7VvqYFYM9uuIm62etac2/i8OpVSww3RVuIDNprJS/iM4BlmA3Y8hdv2EDp5zZy9BIo1Nzx+qAVhpMxasLs/1sEBBDaxRzP6o=",
        "Encryption": {
            "Algorithm": "AES-256-CBC",
            "CiphertextBlob": "sBmIZTmfcZ4FZIskKB1PC3yYx0a/CxBh8KwnQWgsgK96UeHeswIJdH7Gt4LW8yiIUjFq7PdikshkRdYPk9OWWEfAWb70DjfNnWLhI8FMMT72A+V+uWeQZN4VtwWdH6I2FrV4aXYxblq7cHHALvL1Ey8x0Cl9CFBeIrQsBGNnnW8=",
            "EncryptList": [
                "EncryptedBody"
            ],
            "Iv": "U2KHDqXYtpCl3l5BRuH0qw==",
            "TagList": null
        },
        "IdNum": "",
        "Name": "",
        "Nation": "",
        "ReflectDetailInfos": [],
        "RequestId": "9782fbce-de72-4325-8e07-ffb3d540be90",
        "Sex": "",
        "ValidDate": ""
    }
}
```

