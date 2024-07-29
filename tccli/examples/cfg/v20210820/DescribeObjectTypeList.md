**Example 1: 请求对象类型列表**



Input: 

```
tccli cfg DescribeObjectTypeList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ObjectTypeList": [
            {
                "ObjectTypeId": 0,
                "ObjectTypeTitle": "abc",
                "ObjectTypeLevelOne": "abc",
                "ObjectTypeParams": {
                    "Key": "abc",
                    "Fields": [
                        {
                            "Key": "abc",
                            "Header": "abc",
                            "Transfer": "abc",
                            "JsonParse": "abc"
                        }
                    ]
                },
                "ObjectTypeJsonParse": {
                    "NameSpace": "abc",
                    "WorkloadName": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

