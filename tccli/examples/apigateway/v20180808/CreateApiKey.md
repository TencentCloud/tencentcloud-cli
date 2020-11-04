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
            "AccessKeyId": "AKID8my5MRr9i6VM98F3dZG9zV0KuBq5ID7pMG83",
            "AccessKeySecret": "9i3BQU8lMUl2dAvrF8RvL5EM6RKEG47P770du61B",
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

