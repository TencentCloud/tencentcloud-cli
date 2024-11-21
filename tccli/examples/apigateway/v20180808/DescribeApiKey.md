**Example 1: DescribeApiKey**



Input: 

```
tccli apigateway DescribeApiKey --cli-unfold-argument  \
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
        "RequestId": "ac423dbe-4e28-470d-b3f7-b8c95c614124"
    }
}
```

