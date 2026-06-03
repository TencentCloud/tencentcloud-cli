**Example 1: 创建主体**



Input: 

```
tccli vclm CreateAigcElement --cli-unfold-argument  \
    --Name xincheng_0 \
    --Description 这是我的一个主体测试 \
    --ReferenceType image_refer \
    --ElementImageList.ReferImages.0.ImageUrl https://*************************cos-internal.ap-guangzhou.tencentcos.cn**********/82fe54a8-4ebf-4407-b64d-56e675f93d5d.jpeg***************************************************************************************************************************************************************************************************************************** \
    --ElementImageList.FrontalImage https://*************************cos-internal.ap-guangzhou.tencentcos.cn**********/82fe54a8-4ebf-4407-b64d-56e675f93d5d.jpeg***************************************************************************************************************************************************************************************************************************** \
    --Provider kling \
    --TagList.0.TagId o_102
```

Output: 
```
{
    "Response": {
        "CreatedAt": "2026-03-27T21:19:01+08:00",
        "ElementId": "elem_c49a7c2f-d440-4e16-b727-2064e8fb44a4",
        "JobId": "1429096434393178112",
        "Provider": [
            "kling"
        ],
        "Status": "pending",
        "RequestId": "c49a7c2f-d440-4e16-b727-2064e8fb44a4"
    }
}
```

