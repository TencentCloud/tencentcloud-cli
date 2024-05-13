**Example 1: 成功查询**

成功查询

Input: 

```
tccli hunyuan QueryHunyuanImageJob --cli-unfold-argument  \
    --JobId test
```

Output: 
```
{
    "Response": {
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "5",
        "JobStatusMsg": "处理完成",
        "RequestId": "56b2ecae-46e4-4697-87d2-dc2b3bbbc2c6",
        "ResultDetails": [
            "Success"
        ],
        "ResultImage": [
            "https:/result.jpg"
        ],
        "RevisedPrompt": [
            "摄影风格，画面主要描述一座雄伟的山峰，山顶覆盖着白雪，阳光照耀下闪耀着光芒，背景是蔚蓝的天空，镜头是全景"
        ]
    }
}
```

