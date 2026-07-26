**Example 1: 查询结果示例**



Input: 

```
tccli mps DescribeCloneViralTask --cli-unfold-argument  \
    --TaskId 24000191-ViralClone-92e56dab-2a5b-4537-b49f-854563d4903f
```

Output: 
```
{
    "Response": {
        "Status": "DONE",
        "VideoUrls": [
            "https://laurie-tmp-1300828900.cos.ap-nanjing.myqcloud.com/viral_clone/20260720/24000191-ViralClone-92e56dab-2a5b-4537-b49f-854563d4903f/clip.mp4"
        ],
        "RequestId": "74aeda83-63cc-4404-9f10-e43e841d242c"
    }
}
```

