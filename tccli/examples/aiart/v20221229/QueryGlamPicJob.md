**Example 1: 查询美照任务**



Input: 

```
tccli aiart QueryGlamPicJob --cli-unfold-argument  \
    --JobId 251197749-1739792863-ff707c2a-ed24-11ef-b774-525400c5aaa8-0
```

Output: 
```
{
    "Response": {
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "5",
        "JobStatusMsg": "处理完成",
        "RequestId": "fcf5d2a6-bd68-4a86-a931-28dd6322e457",
        "ResultDetails": [
            "Success"
        ],
        "ResultImage": [
            "https://xxx.cos.ap-guangzhou.myqcloud.com/glam_pic/xxx.jpg"
        ]
    }
}
```

