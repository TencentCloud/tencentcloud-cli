**Example 1: 调用示例**



Input: 

```
tccli vclm SubmitVideoEditJob --cli-unfold-argument  \
    --VideoUrl https://cos.ap-guangzhou.myqcloud.com/xxx.mp4 \
    --Prompt Edit the object in the video \
    --Image.Url https://cos.ap-guangzhou.myqcloud.com/xxx.png
```

Output: 
```
{
    "Response": {
        "JobId": "1390601287988002816",
        "RequestId": "33de6b6d-99cd-498c-a3b2-f31db1e94ab8"
    }
}
```

