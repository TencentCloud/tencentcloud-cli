**Example 1: 解析索引文件**



Input: 

```
tccli vod ParseStreamingManifest --cli-unfold-argument  \
    --MediaManifestContent #EXTM3U\n#EXT-X-TARGETDURATION:10\n#EXTINF:9.009,\nfirst.ts\n#EXTINF:9.009,\nsecond.ts\n#EXT-X-ENDLIST
```

Output: 
```
{
    "Response": {
        "MediaSegmentSet": [
            "first.ts",
            "second.ts"
        ],
        "RequestId": "requestId"
    }
}
```

