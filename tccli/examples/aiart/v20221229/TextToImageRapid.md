**Example 1: 调用示例**



Input: 

```
tccli aiart TextToImageRapid --cli-unfold-argument  \
    --Prompt 画一个小狗 \
    --Resolution 1024:1024 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "RequestId": "e77c02f6-44b1-4e67-a503-844ebb44f067",
        "ResultImage": "https://xxx.cos.ap-guangzhou.myqcloud.com/xxx.jpg",
        "Seed": 4180030109
    }
}
```

