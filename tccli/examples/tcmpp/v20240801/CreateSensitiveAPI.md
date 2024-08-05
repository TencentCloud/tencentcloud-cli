**Example 1: demo**

demo

Input: 

```
tccli tcmpp CreateSensitiveAPI --cli-unfold-argument  \
    --ApplicationId abc \
    --ApiList.0.ApiName abc \
    --ApiList.0.ApiDesc abc \
    --ApiList.0.ApiType 0 \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "abc"
    }
}
```

