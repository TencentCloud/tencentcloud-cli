**Example 1: 获取某一产品发布过的全部固件版本**



Input: 

```
tccli iotvideo DescribePubVersions --cli-unfold-argument  \
    --ProductId 12345678910
```

Output: 
```
{
    "Response": {
        "RequestId": "38545b17-d6c7-4bbe-89c2-c43e0fdc4100",
        "Data": [
            {
                "OtaVersion": "1.2.22",
                "PublishTime": 1577276283
            },
            {
                "OtaVersion": "1.2.23",
                "PublishTime": 1578297901
            }
        ]
    }
}
```

