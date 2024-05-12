**Example 1: 请求示例**

接口用于停止垫片流。

Input: 

```
tccli live StopLivePadProcessor --cli-unfold-argument  \
    --PushDomainName 5000.livepush.myqcloud.com \
    --AppName live \
    --StreamName test
```

Output: 
```
{
    "Response": {
        "ResultMessage": "success",
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

