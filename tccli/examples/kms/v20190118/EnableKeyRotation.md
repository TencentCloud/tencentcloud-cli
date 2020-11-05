**Example 1: Enabling key rotation**

This example shows you how to enable key rotation for a specified CMK.

Input: 

```
tccli kms EnableKeyRotation --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

