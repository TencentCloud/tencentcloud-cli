**Example 1: 调用成功示例**



Input: 

```
tccli vclm DescribeVideoExtendKlingJob --cli-unfold-argument  \
    --JobId 1429040713202016256
```

Output: 
```
{
    "Response": {
        "Duration": "10.433",
        "ErrorCode": "",
        "ErrorMessage": "submit ****** ******* ***",
        "FinalUnitDeduction": "2",
        "ResultVideoUrl": "https://*******************.cos.ap-guangzhou.tencentcos.cn/****************/results/**********0ff6f28b-c876-40*9*98d2-ad8b9eda48c7_1774604256.mp4?q-sign-algorithm=sha1&q-ak*******************************lMrLgp&q-sign-time=1774604256%3B1774690656&q-key-time=1774604256%3B1774690656&q-header-list=host&q-url-param-list=&q-signature=39674cf99f549978bf19d00aee72a05762b2dd51",
        "Status": "DONE",
        "RequestId": "ab2bf032-1457-49ec-9560-aa975c831fb3",
        "VideoId": "867555************"
    }
}
```

