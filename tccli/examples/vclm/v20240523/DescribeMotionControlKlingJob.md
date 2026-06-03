**Example 1: 调用成功示例**



Input: 

```
tccli vclm DescribeMotionControlKlingJob --cli-unfold-argument  \
    --JobId 1429083941754249216
```

Output: 
```
{
    "Response": {
        "Duration": "9.066",
        "ErrorCode": "",
        "ErrorMessage": "",
        "FinalUnitDeduction": "4.5",
        "ResultVideoUrl": "https://**g*t**************.cos.ap-guangzhou.tencentcos.cn/videoed**********sults/************9e868f-e479-4ef4-bf25-6d1ef6569b2b_1774614562.mp4?q-sign-algorithm=sha1&q-ak=***********x*******************MrLgp&q-sign-time=1774614562%3B1774700962&q-key-time=1774614562%3B1774700962&q-header-list=host&q-url-param-list=&q-signature=c6352b834071a755c86489c8097e2cc3dafe78c3",
        "Status": "DONE",
        "RequestId": "739f6a7f-35e5-4937-b501-100cf6a10bd2"
    }
}
```

