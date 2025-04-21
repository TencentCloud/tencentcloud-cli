**Example 1: 修改授权**

修改授权

Input: 

```
tccli ioa ModifySoftwareAuth --cli-unfold-argument  \
    --SoftName qq \
    --SoftVersion 1.1 \
    --AuthType 2 \
    --AuthNum 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthName": "qq"
        },
        "RequestId": "17149468-1d9d-49e1-81bf-5562162d95b7"
    }
}
```

