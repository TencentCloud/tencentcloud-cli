**Example 1: DescribeApiKey**



Input: 

```
tccli apigateway DescribeApiKey --cli-unfold-argument  \
    --AccessKeyId AKID1IGx7Tu5mk150ds6fhbdi1RqD8KlI6dW32MD
```

Output: 
```
{
    "Response": {
        "Result": {
            "AccessKeyId": "AKID1IGx7Tu5mk150ds6fhbdi1RqD8KlI6dW32MD",
            "AccessKeySecret": "hvhuan76de5im5Fa0bqh8aaBcOO9cy6c7yg2ywlf",
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

