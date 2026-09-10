**Example 1: 获取云函数地址并下载zip包**



Input: 

```
tccli tcb DownloadFunction --cli-unfold-argument  \
    --FunctionName scfhelloworld \
    --EnvId lowcode-xxx \
    --Qualifier $LATEST
```

Output: 
```
{
    "Response": {
        "SCFErrorCode": "",
        "SCFErrorMsg": "",
        "Url": "https://...",
        "RequestId": "c75d9568-6abf-41ad-91d6-3ab9171e1741"
    }
}
```

