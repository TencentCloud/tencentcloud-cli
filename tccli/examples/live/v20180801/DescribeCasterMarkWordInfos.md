**Example 1: 查询导播台文本列表**



Input: 

```
tccli live DescribeCasterMarkWordInfos --cli-unfold-argument  \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "MarkWordInfos": [
            {
                "MarkWordIndex": 1,
                "MarkWordText": "example mark word",
                "MarkWordFontSize": 52,
                "MarkWordFontColor": "0xd0021b",
                "MarkWordFontType": 1,
                "MarkWordLocationX": 0,
                "MarkWordLocationY": 0.5,
                "MarkWordRollEnable": false,
                "MarkWordRollDirection": 0,
                "MarkWordRollOnceTime": 5,
                "MarkWordRollStartLocationX": 0,
                "MarkWordRollEndLocationX": 0.3
            }
        ],
        "RequestId": "d4040a52-8d42-4a76-8f28-ded6b3fa9a6e"
    }
}
```

