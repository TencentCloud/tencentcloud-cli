**Example 1: Parsing index file**



Input: 

```
tccli vod ParseStreamingManifest --cli-unfold-argument  \
    --MediaManifestContent %23EXTM3U%0D%0A%23EXT-X-TARGETDURATION:10%0D%0A%23EXTINF:9.009%0D%0Afirst.ts%0D%0A%23EXTINF:9.009%0D%0Asecond.ts%0D%0A%23EXT-X-ENDLIST
```

Output: 
```
{
    "Response": {
        "MediaSegmentSet": [
            "first.ts",
            "second.ts"
        ]
    }
}
```

