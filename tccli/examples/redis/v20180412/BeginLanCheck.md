**Example 1: 太过频繁**

太过频繁

Input: 

```
tccli redis BeginLanCheck --cli-unfold-argument  \
    --InstanceId crs-p4w1qhvr
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.InstanceNotExists",
            "Message": "BeginLanCheck timeSpan is too small err: timeSpan is crs-p4w1qhvr"
        },
        "RequestId": "bf9a9dbe-432f-45cf-9643-75b325753e17"
    }
}
```

