**Example 1: 获取发布序列**

获取集群发布序列

Input: 

```
tccli tke DescribeRollOutSequences --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26",
        "TotalCount": 1,
        "Sequences": [
            {
                "ID": 1,
                "Name": "test1",
                "SequenceFlows": [
                    {
                        "Tags": [
                            "Test"
                        ],
                        "SoakTime": 86400
                    },
                    {
                        "Tags": [
                            "Pre-Production"
                        ],
                        "SoakTime": 86400
                    },
                    {
                        "Tags": [
                            "Production"
                        ],
                        "SoakTime": 86400
                    }
                ],
                "Enabled": true
            }
        ]
    }
}
```

