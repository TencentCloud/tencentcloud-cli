**Example 1: 示例**



Input: 

```
tccli wedata ListBatchDetail --cli-unfold-argument  \
    --JobId 1
```

Output: 
```
{
    "Response": {
        "JobId": 1,
        "RunType": "abc",
        "SuccessResource": [
            {
                "ProcessId": "abc",
                "ResourceId": "abc",
                "ResourceName": "abc",
                "ExtraInfo": [
                    {
                        "ParamKey": "abc",
                        "ParamValue": "abc"
                    }
                ]
            }
        ],
        "FailResource": [
            {
                "ProcessId": "abc",
                "ResourceId": "abc",
                "ResourceName": "abc",
                "ExtraInfo": [
                    {
                        "ParamKey": "abc",
                        "ParamValue": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

