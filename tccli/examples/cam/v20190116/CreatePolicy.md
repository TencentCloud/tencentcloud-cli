**Example 1: Creating a policy**

This example shows you how to create a policy that allows all COS APIs to access all COS resources.

Input: 

```
tccli cam CreatePolicy --cli-unfold-argument  \
    --PolicyName test-2019-04-29\
    --Description 'Policy description'\
    --PolicyDocument {"version":"2.0","statement":[{"effect":"allow","action":["name/cos:*"],"resource":["*"]}]}
```

Output: 
```
{
    "Response": {
        "PolicyId": 17698703,
        "RequestId": "89360f78-b1dd-4e43-aa91-ecb2c8b8f282"
    }
}
```

