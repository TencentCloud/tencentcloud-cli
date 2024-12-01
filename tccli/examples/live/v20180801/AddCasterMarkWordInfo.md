**Example 1: 请求实例**



Input: 

```
tccli live AddCasterMarkWordInfo --cli-unfold-argument  \
    --CasterId 1234 \
    --MarkWordInfo.MarkWordIndex 1 \
    --MarkWordInfo.MarkWordFontSize 15 \
    --MarkWordInfo.MarkWordText example \
    --MarkWordInfo.MarkWordFontColor 0x000033 \
    --MarkWordInfo.MarkWordLocationY 0.2 \
    --MarkWordInfo.MarkWordLocationX 0.2 \
    --MarkWordInfo.MarkWordFontType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

