**Example 1: 音频审核明细列表**



Input: 

```
tccli ams DescribeAmsList --cli-unfold-argument  \
    --PageToken xx \
    --Limit 0 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageDirection xx
```

Output: 
```
{
    "Response": {
        "PageToken": "xx",
        "AmsDetailSet": [
            {
                "Content": "xx",
                "Name": "xx",
                "Url": "xx",
                "OperateTime": "xx",
                "Label": [
                    "xx"
                ],
                "OriginalLabel": [
                    "xx"
                ],
                "Operator": "xx",
                "DataForm": 0,
                "DetailCount": 0,
                "RequestId": "xx",
                "TaskID": "xx",
                "Duration": 0,
                "InsertTime": "xx",
                "Thumbnail": "xx"
            }
        ],
        "Total": 0,
        "RequestId": "xx"
    }
}
```

