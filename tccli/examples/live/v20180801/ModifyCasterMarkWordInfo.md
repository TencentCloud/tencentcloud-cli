**Example 1: 请求示例**



Input: 

```
tccli live ModifyCasterMarkWordInfo --cli-unfold-argument  \
    --CasterId 1234 \
    --MarkWordInfo.MarkWordIndex 1 \
    --MarkWordInfo.MarkWordFontSize 18 \
    --MarkWordInfo.MarkWordText Modify example \
    --MarkWordInfo.MarkWordFontColor 0x000033 \
    --MarkWordInfo.MarkWordLocationY 0.15 \
    --MarkWordInfo.MarkWordLocationX 0.15 \
    --MarkWordInfo.MarkWordFontType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

