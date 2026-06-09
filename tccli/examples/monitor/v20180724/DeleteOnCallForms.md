**Example 1: 删除值班表**

删除值班表

Input: 

```
tccli monitor DeleteOnCallForms --cli-unfold-argument  \
    --Module abc \
    --OnCallFormIDs abc
```

Output: 
```
{
    "Response": {
        "FailedOnCallFormIDs": [
            "abc"
        ],
        "SuccessOnCallFormIDs": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

