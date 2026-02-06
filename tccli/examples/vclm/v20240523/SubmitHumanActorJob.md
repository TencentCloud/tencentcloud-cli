**Example 1: 调用示例**



Input: 

```
tccli vclm SubmitHumanActorJob --cli-unfold-argument  \
    --Prompt 画面中的人物正在对着镜头讲话，偶尔做些手势匹配说话的内容 \
    --AudioUrl https://cos.ap-guangzhou.myqcloud.com/xxx.mp3 \
    --ImageUrl https://cos.ap-guangzhou.myqcloud.com/xxx.jpg
```

Output: 
```
{
    "Response": {
        "JobId": "1382369743251030016",
        "RequestId": "6f70a522-09c8-46c9-9e22-e6c2ab23ac3c"
    }
}
```

