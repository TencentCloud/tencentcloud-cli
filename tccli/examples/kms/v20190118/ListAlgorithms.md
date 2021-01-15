**Example 1: 列出当前Region支持的加密方式**



Input: 

```
tccli kms ListAlgorithms --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "460fe7ff-f4db-4509-9b20-208badcfb915",
        "SymmetricAlgorithms": [
            {
                "KeyUsage": "ENCRYPT_DECRYPT",
                "Algorithm": "SM4"
            }
        ],
        "AsymmetricAlgorithms": [
            {
                "KeyUsage": "ASYMMETRIC_DECRYPT_SM2",
                "Algorithm": "SM2"
            },
            {
                "KeyUsage": "ASYMMETRIC_DECRYPT_RSA_2048",
                "Algorithm": "RSA_2048"
            }
        ],
        "AsymmetricSignVerifyAlgorithms": [
            {
                "KeyUsage": "ASYMMETRIC_SIGN_VERIFY_SM2",
                "Algorithm": "SM2"
            }
        ]
    }
}
```

