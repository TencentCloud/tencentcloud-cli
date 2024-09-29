**Example 1: cos 风险预签名**



Input: 

```
tccli secmocker MockNoAuthCommon --cli-unfold-argument  \
    --Content  https://sirius-test-1258344699.cos.ap-guangzhou.myqcloud.com/?q-sign-algorithm=sha1&q-ak=AK
```

Output: 
```
{
    "Response": {
        "Content": "http://test-2222.",
        "RequestId": "9bb1b9c4-f0ab-4ab9-b1ef-2832972c2194"
    }
}
```

