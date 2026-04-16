**Example 1: 查询主体**



Input: 

```
tccli vclm DescribeAigcElement --cli-unfold-argument  \
    --ElementId elem_b9cc80f7-c9aa-41a5-85a6-49c4f0f97f2e
```

Output: 
```
{
    "Response": {
        "CreatedAt": "2026-03-27T21:21:35+08:00",
        "Description": "这是我的一个主体测试",
        "ElementId": "elem_b9cc80f7-c9aa-41a5-85a6-49c4f0f97f2e",
        "ElementImageList": {
            "FrontalImage": "https://********************cos.ap-guangzhou.tencentcos.cn/material/input/1259088371/b9cc80f7-c9aa-41a5-85a6-49c4f0f97f2e_1774617695_0.jpg******************************************************************************************************************************************************************************************************************b407db7759c28a8",
            "ReferImages": [
                {
                    "ImageUrl": "https://********************cos.ap-guangzhou.tencentcos.cn/material/input/1259088371/b9cc80f7-c9aa-41a5-85a6-49c4f0f97f2e_1774617695_1.jpg******************************************************************************************************************************************************************************************************************38c6535a1490d19"
                }
            ]
        },
        "Name": "xincheng_0",
        "Provider": [
            "kling"
        ],
        "ProviderDetails": [
            {
                "ErrorMessage": "",
                "Provider": "kling",
                "Status": "succeed"
            }
        ],
        "ReferenceType": "image_refer",
        "Status": "succeed",
        "TagList": [
            {
                "TagId": "o_102"
            }
        ],
        "UpdatedAt": "2026-03-27T21:21:39+08:00",
        "VideoList": [],
        "RequestId": "9eec7037-8458-40a3-a31b-536e7c377487"
    }
}
```

