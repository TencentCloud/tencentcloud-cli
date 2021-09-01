**Example 1: 创建签章**

创建签章

Input: 

```
tccli ds CreateSeal --cli-unfold-argument  \
    --Module SealMng \
    --Operation CreateSeal \
    --AccountResId dcu-c33uil4apd \
    --ImgUrl https://cloud.tencent.com/
```

Output: 
```
{
    "Response": {
        "RequestId": "c3de36ed-11a8-4aca-9355-d891d9da42ad",
        "SealResId": "dcs-hk6wc1vtir"
    }
}
```

