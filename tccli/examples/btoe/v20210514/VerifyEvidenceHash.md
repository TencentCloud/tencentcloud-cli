**Example 1: BTOE存证内容hash核验**

用户存证内容hash向BTOE核验存证记录的真实性。

Input: 

```
tccli btoe VerifyEvidenceHash --cli-unfold-argument  \
    --EvidenceHash 23eca93c271e6ecf8e24f3b0045436cc6bb7456a715c3bfc6d86fd708518de97
```

Output: 
```
{
    "Response": {
        "RequestId": "121212",
        "Result": true
    }
}
```

