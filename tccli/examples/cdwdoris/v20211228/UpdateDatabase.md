**Example 1: 更新**



Input: 

```
tccli cdwdoris UpdateDatabase --cli-unfold-argument  \
    --DbName xxx \
    --Operation SET_QUOTA \
    --Quota 10T
```

Output: 
```
{
    "Response": {
        "Success": true,
        "Message": "Database quota set successfully.",
        "RequestId": "xxxx-xxxx-xxxx-xxxx"
    }
}
```

