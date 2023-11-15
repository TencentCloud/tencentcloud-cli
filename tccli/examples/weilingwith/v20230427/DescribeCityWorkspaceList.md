**Example 1: 通过行政区id获取项目空间信息**

成功返回示例

Input: 

```
tccli weilingwith DescribeCityWorkspaceList --cli-unfold-argument  \
    --AdministrativeCodeSet 002 \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "ec9a85c9-b887-4481-a318-1c41f7d46733",
        "Result": {
            "WorkspaceSet": [
                {
                    "WorkspaceId": 1016,
                    "ChineseName": "华南园区项目",
                    "Description": "华南园区项目",
                    "Status": 0,
                    "ParkName": "园区简称",
                    "ParkNum": "001",
                    "AdministrativeDetailSet": [
                        {
                            "AdministrativeTypeCode": "QH01",
                            "AdministrativeCode": "440000",
                            "AdministrativeName": "广东省"
                        }
                    ]
                }
            ]
        }
    }
}
```

