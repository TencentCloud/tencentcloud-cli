**Example 1: 稠密关键点接口**



Input: 

```
tccli iai AnalyzeDenseLandmarks --cli-unfold-argument  \
    --Mode 0 \
    --Url http://test.image.myqcloud.com/testA.jpg
```

Output: 
```
{
    "Response": {
        "ImageWidth": 550,
        "ImageHeight": 366,
        "DenseFaceShapeSet": [],
        "X": 375,
        "Y": 37,
        "Width": 63,
        "Height": 82,
        "RequestId": "e2242360-f30e-4103-b861-e8ba63eacadc"
    }
}
```

