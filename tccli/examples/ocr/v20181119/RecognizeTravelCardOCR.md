**Example 1: 通信行程卡识别示例代码**

通信行程卡识别

Input: 

```
tccli ocr RecognizeTravelCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Color": "绿色",
        "ReachedCity": [
            "上海市"
        ],
        "RequestId": "49050856-4804-406b-821b-b3d750de3692",
        "RiskArea": [],
        "Telephone": "150****3634",
        "Time": "2022.07.08 11:11:39"
    }
}
```

