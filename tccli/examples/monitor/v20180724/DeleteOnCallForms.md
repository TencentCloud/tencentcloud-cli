**Example 1: 删除值班表**

删除值班表

Input: 

```
tccli monitor DeleteOnCallForms --cli-unfold-argument  \
    --Module monitor \
    --OnCallFormIDs form-zahdhgjo form-adhdhgjc
```

Output: 
```
{
    "Response": {
        "FailedOnCallFormIDs": [
            "form-zahdhgjo"
        ],
        "SuccessOnCallFormIDs": [
            "form-adhdhgjc"
        ],
        "RequestId": "e3873490-7ca2-4efc-8792-77"
    }
}
```

