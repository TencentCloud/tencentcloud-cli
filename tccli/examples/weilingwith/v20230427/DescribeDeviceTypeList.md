**Example 1: 设备列表类型查询结果**

成功响应

Input: 

```
tccli weilingwith DescribeDeviceTypeList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "7be5626c-d9f9-4883-b4c4-3d77ba2fe281",
        "Result": {
            "Set": [
                {
                    "Code": "w0301006",
                    "IsSubsystem": 0,
                    "Name": "烟感报警器",
                    "ParentCode": "0301",
                    "ParentName": "火灾自动报警及联动系统"
                }
            ]
        }
    }
}
```

