**Example 1: Modifying the description of a specified CMK**

This example shows you how to modify the description of a specified CMK.

Input: 

```
tccli kms UpdateKeyDescription --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01\
    --Description NewDescription
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

