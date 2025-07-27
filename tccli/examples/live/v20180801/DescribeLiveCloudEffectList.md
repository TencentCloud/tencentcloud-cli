**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveCloudEffectList --cli-unfold-argument  \
    --Prompt 小狗
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "EnableCreateNum": 100,
        "TotalNum": 30,
        "InfoList": [
            {
                "Id": "1001",
                "Prompt": "小狗",
                "Flag": "动物",
                "Status": "FINISH",
                "PreviewImageUrl": "http://preview.image.com/pic.jpg",
                "Type": "PGC",
                "CreateTime": "2025-05-19T00:00:00Z",
                "UpdateTime": "2025-05-20T00:00:00Z"
            }
        ]
    }
}
```

