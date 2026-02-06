**Example 1: 请求示例**



Input: 

```
tccli live InsertTaskTemporaryFiles --cli-unfold-argument  \
    --TaskId 895451 \
    --InsertAfterIndex 0 \
    --TemporaryFiles http://vod.com/path/test.mp4 \
    --Operator admin
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

