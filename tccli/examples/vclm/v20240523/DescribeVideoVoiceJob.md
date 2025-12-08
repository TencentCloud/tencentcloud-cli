**Example 1: 调用成功示例**

调用成功示例

Input: 

```
tccli vclm DescribeVideoVoiceJob --cli-unfold-argument  \
    --JobId 1372503633131323392
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "45f7928c-eefb-477c-a632-eadec7322b1e",
        "ResultVideoUrl": "https://vcg-test-1258344699.cos.ap-guangzhou.tencentcos.cn/video_voice/results/228a7e.mp4",
        "Status": "DONE"
    }
}
```

