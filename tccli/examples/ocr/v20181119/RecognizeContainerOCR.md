**Example 1: 集装箱识别示例代码**

集装箱识别

Input: 

```
tccli ocr RecognizeContainerOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "ContainerId": "APHU7042391",
        "ContainerType": "45G1",
        "GrossKG": "32500KG",
        "GrossLB": "71650LB",
        "PayloadKG": "28630KG",
        "PayloadLB": "63120LB",
        "TareKG": "3870KG",
        "TareLB": "8530LB",
        "CapacityM3": "76.4CUM",
        "CapacityFT3": "2700CUFT",
        "Warn": [
            -9926,
            -9927
        ],
        "RequestId": "45afaba3-5fb8-480e-83f9-2681f1373783"
    }
}
```

