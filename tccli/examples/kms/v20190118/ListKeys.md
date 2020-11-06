**Example 1: Getting CMK list**

This example shows you how to get the list of CMKs.

Input: 

```
tccli kms ListKeys --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00",
        "Keys": [
            {
                "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01"
            },
            {
                "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b02"
            }
        ],
        "TotalCount": 100
    }
}
```

