**Example 1: Querying Identity Provider Details**

Querying identity provider details

Input: 

```
tccli cam GetSAMLProvider --cli-unfold-argument  \
    --Name okta
```

Output: 
```
{
    "Response": {
        "Name": "okta",
        "Description": "okta",
        "CreateTime": "2018-09-17 17:18:03",
        "ModifyTime": "2018-09-17 17:18:03",
        "SAMLMetadata": "U0FNTE1ldGFkYXRh"
    }
}
```

