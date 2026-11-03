**Example 1: 删除**

删除

Input: 

```
tccli ssl BatchDeleteCSR --cli-unfold-argument  \
    --CSRIds 11 22 33
```

Output: 
```
{
    "Response": {
        "Success": [
            22,
            33
        ],
        "RequestId": "5779b652-9c64-45b3-a6f4-641db7376a2e"
    }
}
```

