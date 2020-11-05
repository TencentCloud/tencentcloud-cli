**Example 1: Disabling key rotation**

This example shows you how to disable key rotation for a specified CMK.

Input: 

```
tccli kms DisableKeyRotation --cli-unfold-argument  \
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

