**Example 1: 绑定号码呼入回调接口**



Input: 

```
tccli ccc BindNumberCallInInterface --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --Number 0086075586013388 \
    --CallInInterface.URL https://cloud.tencent.com/
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

