**Example 1: Querying key rotation status**

This example shows you how to query whether key rotation is enabled for a specified CMK.

Input: 

```
tccli kms GetKeyRotationStatus --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01
```

Output: 
```
{
    "Response": {
        "KeyRotationEnabled": false,
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

