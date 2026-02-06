**Example 1: 查询文生图任务**



Input: 

```
tccli aiart QueryTextToImageJob --cli-unfold-argument  \
    --JobId 1344213737283272704
```

Output: 
```
{
    "Response": {
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "5",
        "JobStatusMsg": "处理完成",
        "RequestId": "e4a4eef5-f4aa-40ff-aae0-5e51c5ef5b1e",
        "ResultDetails": [
            "Success"
        ],
        "ResultImage": [
            "https://cos.ap-guangzhou.myqcloud.com/xxx.jpg"
        ],
        "RevisedPrompt": [
            "一只可爱的小狗正蹲在草地上，它的小耳朵竖立着，鼻子微微皱起，显得十分警觉，小狗的毛色是鲜亮的红色"
        ]
    }
}
```

