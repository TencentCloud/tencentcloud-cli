**Example 1: 提交生视频任务示例**



Input: 

```
tccli vclm SubmitAigcVideoJob --cli-unfold-argument  \
    --Vendor VO \
    --Model V3.1 \
    --ModelParam {
"image":"https://**********************-guangzhou.myqcloud.com/****.jpeg",
"resolution":"1080p",
"images":["https://**********************-guangzhou.myqcloud.com/****.jpeg"]
} \
    --Prompt 美女在沙滩跳舞 \
    --LogoAdd 0
```

Output: 
```
{
    "Response": {
        "JobId": "1412464707775373312",
        "RequestId": "bb40df7c-c705-4bf1-b0d6-196e17dfef10"
    }
}
```

