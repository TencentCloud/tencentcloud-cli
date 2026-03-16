**Example 1: ModifyAIMCredential**

ModifyAIMCredential

Input: 

```
tccli apis ModifyAIMCredential --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID crd-8b468a40 \
    --Name newname
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "crd-8b468a40"
        },
        "RequestId": "8b747f07-19ab-4be4-8d0a-0daf862a187b"
    }
}
```

