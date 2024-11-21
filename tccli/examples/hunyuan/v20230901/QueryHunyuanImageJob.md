**Example 1: 成功查询**

成功查询

Input: 

```
tccli hunyuan QueryHunyuanImageJob --cli-unfold-argument  \
    --JobId 251197749-1731412663-d4e1f224-fa21-40bc-9ee7-4bb13abece6e-0
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
            "https://aiart-xxx.cos.ap-guangzhou.myqcloud.com/xxx?q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1731655045;1731658645&q-key-time=1731655045;1731658645&q-header-list=host&q-url-param-list=&q-signature=72776438be444f9a72e04e5e6376aadf51e65655"
        ],
        "RevisedPrompt": [
            "一条细长的小路穿梭在茂密的竹林中，天空下着细雨，雨水滴答落在翠绿的竹叶上，沿途的小路湿润且闪烁着水光，竹叶摇曳间洒下点点水珠，营造出静谧而清新的氛围"
        ]
    }
}
```

