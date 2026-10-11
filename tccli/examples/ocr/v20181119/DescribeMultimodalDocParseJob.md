**Example 1: 查询任务成功示例**



Input: 

```
tccli ocr DescribeMultimodalDocParseJob --cli-unfold-argument  \
    --TaskId 1493508761820692480
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "FailPageNum": 0,
        "ResultUrl": "https://ocr-smartdoc-1258344699.cos.ap-guangzhou.myqcloud.com/multimodal-doc-parse/result/251138**0/1493508761820692480/result.zip?q-sign-algorithm=sha1&q-ak=*KID1o*JyNjUcV7UbSNLo69woR0KPzLSF*VG&q-sign-time=178997464*%3B1*8*9*6447&q-key-time=17899746**%3B1789976447&q-header-list=host&q-url-param-list=&q-signature=f986bbc310f7684eef0c359a36ae5b09f35c8a68",
        "Status": "Success",
        "SuccessPageNum": 1,
        "RequestId": "376ecd73-a87f-4f61-8075-8d94260161e9"
    }
}
```

