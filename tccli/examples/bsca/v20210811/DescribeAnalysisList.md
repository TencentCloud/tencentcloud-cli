**Example 1: 查询分析项列表**

查询分析项信息，限制返回结果最多为一项。

Input: 

```
tccli bsca DescribeAnalysisList --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AnalysisSet": [
            {
                "AnalysisId": "4a49ab59-cea9-4d19-bed3-326a27465d92",
                "AnalysisName": "MyAnalysis",
                "AnalysisType": "GENERIC",
                "AnalysisParam": "",
                "FileName": "demo.img",
                "FileSize": 20408884,
                "AnalysisState": "SUCCESS",
                "Star": false,
                "Tags": [
                    {
                        "Key": "tagKey1",
                        "Value": "tagValue1"
                    },
                    {
                        "Key": "tagKey2",
                        "Value": "tagValue2"
                    }
                ],
                "UpdatedTime": "2021-10-29T11:52:40Z",
                "CVECount": {
                    "CriticalCount": 11,
                    "HighCount": 168,
                    "MediumCount": 317,
                    "LowCount": 21
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "97187deb-a9fb-4bf7-8ade-2d3f9fed7467"
    }
}
```

