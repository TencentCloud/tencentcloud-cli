**Example 1: UpdateApiKey**



Input: 

```
tccli apigateway UpdateApiKey --cli-unfold-argument  \
    --AccessKeyId AKID***********************************************
```

Output: 
```
{
    "Response": {
        "Result": {
            "AccessKeyId": "AKID***********************************************",
            "AccessKeySecret": "qYSyjR************************************",
            "AccessKeyType": "auto",
            "SecretName": "dd",
            "Status": 1,
            "CreatedTime": "2020-02-26T06:09:44Z",
            "ModifiedTime": "2020-02-26T06:45:57Z"
        },
        "RequestId": "3d0d6dc0-1fa9-4634-9c42-a1ff635c0bd5"
    }
}
```

