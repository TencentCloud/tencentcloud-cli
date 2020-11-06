**Example 1: Creating a CMK**

This example shows you how to create a CMK used for data key management. The CMK can be used in other APIs to create data keys, perform encryption and decryption, and do more.

Input: 

```
tccli kms CreateKey --cli-unfold-argument  \
    --Alias mykey \
    --KeyUsage ENCRYPT_DECRYPT \
    --Description test
```

Output: 
```
{
    "Response": {
        "KeyId": "9999aed0-4956-11e9-bc70-5254005e86b4",
        "Alias": "alias-0001",
        "CreateTime": 1552897190,
        "Description": "test cmk",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "RequestId": "850bf779-2249-4995-8c55-b3966daf0a8c"
    }
}
```

