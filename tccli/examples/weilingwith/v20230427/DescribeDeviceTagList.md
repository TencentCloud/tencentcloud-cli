**Example 1: 设备标签列表查询**

正常响应

Input: 

```
tccli weilingwith DescribeDeviceTagList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 1 \
    --ApplicationToken YVySZSL1Lp5UtSJ5uJVLJYOKDEGfCCH2
```

Output: 
```
{
    "Response": {
        "RequestId": "e812b515-ad1d-496a-9042-4494c4c8128e",
        "Result": {
            "PageNumber": 1,
            "PageSize": 1,
            "Set": [
                {
                    "TagId": 35,
                    "TagName": "西安真实摄像头"
                }
            ],
            "TotalPage": 43,
            "TotalRow": 43
        }
    }
}
```

