**Example 1: GetAIMCredential**

GetAIMCredential

Input: 

```
tccli apis GetAIMCredential --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID crd-0d1e5311
```

Output: 
```
{
    "Response": {
        "Data": {
            "Credentials": [
                {
                    "Key": "TmpSecretId",
                    "Value": "AKID************************************************************D2Om"
                }
            ]
        },
        "RequestId": "1628a9e7-8854-44c5-adce-047a770ea943"
    }
}
```

