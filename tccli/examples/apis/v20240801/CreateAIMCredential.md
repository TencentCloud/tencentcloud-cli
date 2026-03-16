**Example 1: CreateAIMCredential**

CreateAIMCredential-access

Input: 

```
tccli apis CreateAIMCredential --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --Name testaccess \
    --Type access \
    --Access.0.Key testkey \
    --Access.0.Value testvalue \
    --Tags testtag
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "crd-8b468a40"
        },
        "RequestId": "9d1c7b14-6fa4-4257-881c-78cba1e8802f"
    }
}
```

