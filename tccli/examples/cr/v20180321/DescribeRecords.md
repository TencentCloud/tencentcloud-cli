**Example 1: 查看录音列表**



Input: 

```
tccli cr DescribeRecords --cli-unfold-argument  \
    --Module Record \
    --Operation List \
    --StartBizDate 2019-03-03 \
    --EndBizDate 2019-03-13 \
    --Offset 0 \
    --Limit 10 \
    --InstId ins-a1b2c3
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "AccountNum": "QK071200000001",
                "BizDate": "2019-03-05",
                "CallStartTime": "2019-03-05 13:00:00",
                "CallerPhone": "01055553333",
                "Direction": "O",
                "Duration": 15,
                "ProductId": null,
                "RecordCosUrl": "http://cr.cosgz.myqcloud.com/cnc/cr-record-ab-f30"
            }
        ],
        "RequestId": "",
        "TotalCount": 1
    }
}
```

