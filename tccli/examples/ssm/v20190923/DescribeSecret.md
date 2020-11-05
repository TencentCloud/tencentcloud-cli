**Example 1: Obtaining detailed information of a Secret**



Input: 

```
tccli ssm DescribeSecret --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "RequestId": "92ad8e05-8eee-475b-9cc9-48035f6310e1",
        "SecretName": "test",
        "Description": "description",
        "KmsKeyId": "13437ab9-e002-11e9-9936-5254006d0810",
        "CreateUin": 3350000000,
        "Status": "Disabled",
        "DeleteTime": 0,
        "CreateTime": 1574160561
    }
}
```

