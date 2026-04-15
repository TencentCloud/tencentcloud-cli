**Example 1: 示例**



Input: 

```
tccli vclm SubmitImageToVideoJob --cli-unfold-argument  \
    --Image.Url https://cqicchen-test-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/neckyang/templatetovideo/downson.png?q-sign-algorithm=sha1&q-ak=*****&q-sign-time=1774494815;1774502015&q-key-time=1774494815;1774502015&q-header-list=host&q-url-param-list=&q-signature=**** \
    --CameraControl.Type simple
```

Output: 
```
{
    "Response": {
        "JobId": "1428581788753207296",
        "RequestId": "b867e180-074e-4b7d-a275-cc5c0032931c"
    }
}
```

