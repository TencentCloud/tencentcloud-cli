**Example 1: Forbidding a media file**



Input: 

```
tccli vod ForbidMediaDistribution --cli-unfold-argument  \
    --FileIds 7447398156998994860 \
    --SubAppId 1 \
    --Operation forbid
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-1d4b-5594145287e1",
        "NotExistFileIdSet": []
    }
}
```

