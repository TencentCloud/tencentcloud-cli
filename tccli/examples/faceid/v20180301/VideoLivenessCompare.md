**Example 1: 静默活体人脸比对**



Input: 

```
tccli faceid VideoLivenessCompare --cli-unfold-argument  \
    --ImageUrl <ImageUrl> \
    --VideoUrl <VideoUrl> \
    --LivenessType SILENT \
    --ImageMd5 682e24b207acf1825286c1fceef5631c \
    --VideoMd5 682e24b207acf1825286c1fceef5631c
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "成功",
        "BestFrame": {
            "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
            "MD5": "682e24b207acf1825286c1fceef5631c",
            "Size": 9430792
        },
        "Sim": 89.88,
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

