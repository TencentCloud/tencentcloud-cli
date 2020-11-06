**Example 1: 确认上传成功例子**



Input: 

```
tccli vod CommitUpload --cli-unfold-argument  \
    --VodSessionKey 3KEGq9DWHl1xF819mM4jVFkGn5WON80NwN/rTrx56UoEFApIV9DQ7t5m1g4hASR11gKWwGxkignB3AmhKOpUnym7wyNEHOwDJPcT5fBu66iCLcW7bhyRfDSsQcVpX0Wt96RKSsZFf62jeAB+e5640U8rMPV3Rf2eR+y1AgI+EC3JZU5iZbjLX4qNVI4R \
    --SubAppId 1
```

Output: 
```
{
    "Response": {
        "FileId": "24820810452266399",
        "MediaUrl": "http://251000333.vod2.myqcloud.com/6c0f1c00vodgzp251000333/dee2125c24820810452266399/f0.mp4",
        "CoverUrl": "http://251000333.vod2.myqcloud.com/6c0f1c00vodgzp251000333/dee2125c24820810452266399/24820810452266400.jpg",
        "RequestId": "requestId"
    }
}
```

