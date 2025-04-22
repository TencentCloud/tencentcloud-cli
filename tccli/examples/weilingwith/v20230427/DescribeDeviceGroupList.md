**Example 1: 测试环境demo**

测试环境demo

Input: 

```
tccli weilingwith DescribeDeviceGroupList --cli-unfold-argument  \
    --ApplicationToken MZb6GZZtBTSI6mkwPqXVLggUOb0qAI3F \
    --WorkspaceId 1016
```

Output: 
```
{
    "Response": {
        "RequestId": "c0461157-50dc-4f20-aa1e-eebd26884645",
        "Result": {
            "List": [
                {
                    "Description": "",
                    "Id": 63,
                    "Name": "test1",
                    "ParentId": 0
                },
                {
                    "Description": "",
                    "Id": 64,
                    "Name": "test2",
                    "ParentId": 62
                },
                {
                    "Description": "",
                    "Id": 65,
                    "Name": "test3",
                    "ParentId": 64
                },
                {
                    "Description": "",
                    "Id": 66,
                    "Name": "test4",
                    "ParentId": 64
                },
                {
                    "Description": "",
                    "Id": 70,
                    "Name": "test5",
                    "ParentId": 0
                },
                {
                    "Description": "",
                    "Id": 62,
                    "Name": "test6",
                    "ParentId": 0
                }
            ]
        }
    }
}
```

