**Example 1: Canceling stream mix**

This example shows you how to cancel a stream mix by session ID.

Input: 

```
tccli live CancelCommonMixStream --cli-unfold-argument  \
    --MixStreamSessionId test_room
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

