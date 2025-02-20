**Example 1: 提交美照任务**



Input: 

```
tccli aiart SubmitGlamPicJob --cli-unfold-argument  \
    --TemplateUrl https://xxx.com/template.jpg \
    --FaceInfos.0.ImageUrls https://xxx.com/input.jpg \
    --Num 1 \
    --Similarity 0.6
```

Output: 
```
{
    "Response": {
        "JobId": "251197749-1739859949-31f02502-edc1-11ef-a849-525400c5aaa8-0",
        "RequestId": "d878c2e1-7108-40b5-aecf-4fb37a6e5695"
    }
}
```

