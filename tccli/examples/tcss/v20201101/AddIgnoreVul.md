**Example 1: 新增漏洞扫描忽略漏洞**



Input: 

```
tccli tcss AddIgnoreVul --cli-unfold-argument  \
    --List.0.PocID "xx" \
    --List.0.ImageIDs "xx" \
    --List.0.ImageType "xx"
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

