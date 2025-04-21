**Example 1: DescribeAuthSourceSelected**



Input: 

```
tccli ioa DescribeAuthSourceSelected --cli-unfold-argument  \
    --PolicyType 1 \
    --PolicyId 13 \
    --GroupId 113
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthSourceSelected": [
                {
                    "AuthState": 2,
                    "TerminalType": 1,
                    "AuthSourceArray": []
                },
                {
                    "AuthState": 1,
                    "TerminalType": 1,
                    "AuthSourceArray": [
                        {
                            "AuthSourceName": "iOA本地账密",
                            "AuthSourceGuid": "iOA",
                            "AuthSourceId": 5
                        }
                    ]
                },
                {
                    "AuthState": 2,
                    "TerminalType": 2,
                    "AuthSourceArray": []
                },
                {
                    "AuthState": 1,
                    "TerminalType": 2,
                    "AuthSourceArray": [
                        {
                            "AuthSourceName": "iOA本地账密",
                            "AuthSourceGuid": "iOA",
                            "AuthSourceId": 5
                        }
                    ]
                }
            ]
        },
        "RequestId": "37f257ee-72d9-493c-b47b-32c3518da09b"
    }
}
```

