**Example 1: 获取查重结果调用成功**



Input: 

```
tccli iai GetSimilarPersonResult --cli-unfold-argument  \
    --JobId YP6v5v32pvyAqLyz
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "SimilarPersonsUrl": "https://sendto-mergeperson-result-test-1254418846.cos.ap-guangzhou.myqcloud.com/251006443_YP6v5v32pvyAqLyz.json?q-sign-algorithm=sha1&q-ak=AKIDl23oKapR0JM8zkElxta1EI7f3GSWDFiv&q-sign-time=1574996201;1574996501&q-key-time=1574996201;1574996501&q-header-list=&q-url-param-list=&q-signature=323f6d761675189ae2285faf04fa8fcef32a6f76",
        "RequestId": "9cf173a5-4ae5-46fb-9898-6c876263780d"
    }
}
```

**Example 2: 获取查重结果调用失败**



Input: 

```
tccli iai GetSimilarPersonResult --cli-unfold-argument  \
    --JobId AAAAAAAAAAAA
```

Output: 
```
{
    "Response": {
        "RequestId": "b0b17778-2f4a-4286-9896-5b1732513c71"
    }
}
```

