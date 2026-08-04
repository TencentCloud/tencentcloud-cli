**Example 1: 立即轮转密钥**

立即轮转密钥

Input: 

```
tccli kms RotateKey --cli-unfold-argument  \
    --KeyId 6ce625e3-01a4-11f1-9481-525400faed4b
```

Output: 
```
{
    "Response": {
        "TaskId": "3027e0ed-28f1-11f1-b397-525400796650",
        "RequestId": "a09e3218-fb08-4560-8377-189e1b791032"
    }
}
```

