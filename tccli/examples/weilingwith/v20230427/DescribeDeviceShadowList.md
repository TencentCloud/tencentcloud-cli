**Example 1: 设备影子查询**

正常响应

Input: 

```
tccli weilingwith DescribeDeviceShadowList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --WIDSet 026d1dd8-a6d7-4fb7-9a94-0df07edaaff8 \
    --PageNumber 1 \
    --PageSize 20 \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "16528537-3858-42bd-973a-ae8c80bdeee3",
        "Result": {
            "PageNumber": 1,
            "PageSize": 20,
            "Set": [
                {
                    "DeviceShadow": "x-json:{\"desired\":{},\"reported\":{\"events\":{},\"profile\":{\"modelId\":\"w0745001\"},\"properties\":{\"Ept\":96,\"IA\":32,\"IB\":42},\"reportTs\":1693370542126}}",
                    "DeviceShadowUpdateTime": "2023-08-30 12:42:22",
                    "WID": "026d1dd8-a6d7-4fb7-9a94-0df07edaaff8"
                }
            ],
            "TotalPage": 1,
            "TotalRow": 1
        }
    }
}
```

