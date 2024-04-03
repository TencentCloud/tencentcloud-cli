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
                    "Name": "testqy111",
                    "ParentId": 0
                },
                {
                    "Description": "",
                    "Id": 64,
                    "Name": "testqy111dadad",
                    "ParentId": 62
                },
                {
                    "Description": "",
                    "Id": 65,
                    "Name": "testqy111dadad11666655",
                    "ParentId": 64
                },
                {
                    "Description": "",
                    "Id": 66,
                    "Name": "testqy111dadad11666",
                    "ParentId": 64
                },
                {
                    "Description": "",
                    "Id": 70,
                    "Name": "3213",
                    "ParentId": 0
                },
                {
                    "Description": "",
                    "Id": 62,
                    "Name": "testqy",
                    "ParentId": 0
                }
            ]
        }
    }
}
```

