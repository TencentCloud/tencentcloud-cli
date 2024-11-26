**Example 1: 会话记录**



Input: 

```
tccli lke GetMsgRecord --cli-unfold-argument  \
    --Type 2 \
    --Count 15 \
    --SessionId your session id \
    --LastRecordId 
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Content": "用户查询",
                "RecordId": "9415678e-1ac5-4987-ac86-d8f9c001c93c",
                "RelatedRecordId": "H9I_20241107_201302_963_b8oJXfpL",
                "IsFromSelf": true,
                "FromName": "用户A",
                "FromAvatar": "https://qidian-qbot-xxxxxx.cos.ap-guangzhou.myqcloud.com/public/174434244193038090240/1801166482343244637056/image/jNVJvoXsTsBzo2324324121HZdgd-1816016475183120384.png",
                "Timestamp": "1730981587",
                "HasRead": true,
                "Score": 1,
                "CanRating": true,
                "Type": 1,
                "References": [
                    {
                        "Id": "1856329177919861888",
                        "Url": "",
                        "Type": 2,
                        "Name": "我的文档",
                        "DocId": "25395"
                    }
                ],
                "Reasons": [
                    "原因信息"
                ],
                "IsLlmGenerated": true,
                "ImageUrls": [
                    ""
                ]
            }
        ],
        "RequestId": "47d378d4-49b5-454b-a381-088e7015f411"
    }
}
```

