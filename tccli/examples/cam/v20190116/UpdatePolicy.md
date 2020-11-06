**Example 1: Updating a policy**

This example shows you how to update a policy to allow the user to access any COS resources with any COS API.

Input: 

```
tccli cam UpdatePolicy --cli-unfold-argument  \
    --PolicyId 17698703 \
    --PolicyDocument %7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22effect%22%3A%22allow%22%2C%22action%22%3A%5B%22name%2Fcos%3A%2A%22%5D%2C%22resource%22%3A%5B%22%2A%22%5D%7D%5D%7D
```

Output: 
```
{
    "Response": {
        "RequestId": "60e60a86-af67-4bbe-8377-7024a0e1d4c7"
    }
}
```

