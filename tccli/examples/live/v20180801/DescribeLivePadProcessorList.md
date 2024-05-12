**Example 1: 请求示例**

查询正在拉垫片的流。

Input: 

```
tccli live DescribeLivePadProcessorList --cli-unfold-argument  \
    --PushDomainName 5000.livepush.com \
    --AppName live
```

Output: 
```
{
    "Response": {
        "StreamNameList": [
            "test1",
            "test2"
        ],
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

