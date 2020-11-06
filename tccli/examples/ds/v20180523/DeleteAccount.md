**Example 1: 删除帐号**

删除帐号

Input: 

```
tccli ds DeleteAccount --cli-unfold-argument  \
    --Module AccountMng \
    --Operation DeleteAccount \
    --AccountList dcu-9mxcxewm77
```

Output: 
```
{
    "Response": {
        "DelFailedList": [],
        "DelSuccessList": [
            "dcu-9mxcxewm77"
        ],
        "RequestId": "341ec462-4d68-4403-8823-2a6582230f20"
    }
}
```

