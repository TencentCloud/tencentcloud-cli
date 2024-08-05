**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeTempSecret4UploadFile2Cos --cli-unfold-argument  \
    --BusinessName tcmpp \
    --Suffix .png \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Bucket": "abc",
            "Region": "abc",
            "Path": "abc",
            "TempSecretId": "abc",
            "TempSecretKey": "abc",
            "Token": "abc"
        },
        "RequestId": "abc"
    }
}
```

