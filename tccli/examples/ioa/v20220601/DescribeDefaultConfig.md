**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDefaultConfig --cli-unfold-argument  \
    --Names ClientLoginIdentify
```

Output: 
```
{
    "Response": {
        "RequestId": "bc53bc25-dfdf-46bb-be75-66975d802c40",
        "Data": {
            "Items": [
                {
                    "Description": "",
                    "Name": "ClientLoginIdentify",
                    "CreateTime": "2022-07-19 11:09:50",
                    "Value": "{\"Account\":\"1\",\"Mobile\":\"0\",\"Email\":\"0\"}",
                    "UpdateTime": "2022-07-19 11:09:50",
                    "Id": 120
                }
            ]
        }
    }
}
```

