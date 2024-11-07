**Example 1: CreateApiKey**



Input: 

```
tccli apigateway CreateApiKey --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "Result": {
            "AccessKeyId": "AKID***********************************************",
            "AccessKeySecret": "qYSyjR************************************",
            "AccessKeyType": "auto",
            "SecretName": "test",
            "Status": 1,
            "CreatedTime": "2020-02-26T06:10:01Z",
            "ModifiedTime": "2020-02-26T06:10:01Z"
        },
        "RequestId": "ad5218b4-edc3-4195-ba4d-a0ef176783ba"
    }
}
```

