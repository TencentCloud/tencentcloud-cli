**Example 1: Canceling schedule deletion**

This example shows you how to cancel the schedule deletion for a CMK.

Input: 

```
tccli kms CancelKeyDeletion --cli-unfold-argument  \
    --KeyId "23e80852-1e38-11e9-b129-5cb9019b4b01"
```

Output: 
```
{
    "Response": {
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01"
    }
}
```

