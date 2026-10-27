**Example 1: BindInstances**



Input: 

```
tccli cvd BindInstances --cli-unfold-argument  \
    --UserIds usera \
    --InstanceIds cdi-a \
    --InstanceType S1L.LARGE8
```

Output: 
```
{
    "Response": {
        "BindInfoList": [
            {
                "InstanceId": "cdi-a",
                "BindStatus": "BOUND",
                "DisplayName": "cdi-a",
                "UserName": "usera",
                "UserId": "usera"
            }
        ],
        "RequestId": "rid"
    }
}
```

