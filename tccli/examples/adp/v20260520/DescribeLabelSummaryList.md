**Example 1: 查询标签列表**

查询标签列表

Input: 

```
tccli adp DescribeLabelSummaryList --cli-unfold-argument  \
    --KbId 2067622575842400832 \
    --PageNumber 0 \
    --PageSize 1000
```

Output: 
```
{
    "Response": {
        "LabelList": [
            {
                "LabelId": "2092176729458955969",
                "Name": "来源",
                "TermTotalCount": 1,
                "TermList": [
                    {
                        "TermId": "2092176729458955968",
                        "Term": "来源1",
                        "SynonymList": [
                            "来源11"
                        ]
                    }
                ],
                "RefCount": 0,
                "MetaValue": null
            }
        ],
        "TotalCount": 12,
        "RequestId": "3f0e3632-afb5-4ffb-af63-9c086752d5d8"
    }
}
```

