**Example 1: Disabling CMKs in batches**

This example shows you how to disable the CMKs on a specified list in batches.

Input: 

```
tccli kms DisableKeys --cli-unfold-argument  \
    --KeyIds 23e80852-1e38-11e9-b129-5cb9019b4b01 23e80852-1e38-11e9-b129-5cb9019b4b02
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

