**Example 1: DescribeApiKeysStatus**



Input: 

```
tccli apigateway DescribeApiKeysStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ApiKeySet": [
                {
                    "AccessKeyId": "AKID***********************************************",
                    "AccessKeySecret": "qYSyjR************************************",
                    "AccessKeyType": "auto",
                    "SecretName": "dd",
                    "Status": 1,
                    "CreatedTime": "2020-02-26T06:09:44Z",
                    "ModifiedTime": "2020-02-26T06:09:44Z"
                }
            ]
        },
        "RequestId": "6096c75d-1562-44be-a4af-75b5e235d319"
    }
}
```

