**Example 1: 拉取结果**



Input: 

```
tccli faceid GetLivenessResult --cli-unfold-argument  \
    --SdkToken D2B55F0C-FB5D-4FB6-8765-3E931EBBFC79
```

Output: 
```
{
    "Response": {
        "Video": {
            "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
            "MD5": "682e24b207acf1825286c1fceef5631c",
            "Size": 9430792
        },
        "BestFrame": {
            "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
            "MD5": "667c2448b10b09ee9ec14ab2b0d36608",
            "Size": 232267
        },
        "Description": "Failed to call the liveness engine",
        "RequestId": "b8cb2269-08b2-426c-8be8-c7142c7e64e4",
        "Result": "1001"
    }
}
```

