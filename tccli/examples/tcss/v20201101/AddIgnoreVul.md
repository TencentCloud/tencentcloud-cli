**Example 1: 新增漏洞扫描忽略漏洞**



Input: 

```
tccli tcss AddIgnoreVul --cli-unfold-argument  \
    --List.0.PocID "pcmgr-70064" \
    --List.0.ImageIDs "sha256:80beff5ff34259ceb7fbe9cd10b2d94912618f5b5595f234349c5bb0cd4f9211" \
    --List.0.ImageType "2"
```

Output: 
```
{
    "Response": {
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

