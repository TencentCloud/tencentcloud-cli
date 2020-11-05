**Example 1: Modifying alias**

This example shows you how to modify the alias of a specified CMK.

Input: 

```
tccli kms UpdateAlias --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01\
    --Alias NewAlias
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

