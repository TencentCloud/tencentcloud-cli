**Example 1: 通过业务层对象ID获取DID标识**

通过业务层对象ID获取DID标识

Input: 

```
tccli tdid GetTDidByObjectId --cli-unfold-argument  \
    --ObjectId user-test \
    --DAPId 5
```

Output: 
```
{
    "Response": {
        "RequestId": "ebfe20e0-c4bd-4bd3-994b-cf82922af82c",
        "Did": "did:tdid:w1:0x89217ab1a8943dcbcb6e6ec8f7a762e787a944f9"
    }
}
```

