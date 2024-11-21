**Example 1: 获取终端节点列表**



Input: 

```
tccli privatedns DescribeEndPointList --cli-unfold-argument  \
    --Limit 200 \
    --Offset 0 \
    --Filters.0.Name EndPointName \
    --Filters.0.Values 终端节点名 \
    --Filters.1.Name EndPointId \
    --Filters.1.Values eid-24ed8e6319 \
    --Filters.2.Name EndPointServiceId \
    --Filters.2.Values vpcsvc-prvrnrlt \
    --Filters.3.Name EndPointVip \
    --Filters.3.Values 11.149.7.14 11.149.7.141
```

Output: 
```
{
    "Response": {
        "RequestId": "8a4ea9cc-b1df-f8f8-ffe7efbe98f9ff85",
        "TotalCount": 5,
        "EndPointSet": [
            {
                "EndPointId": "eid-24ed8e6319",
                "EndPointName": "名称",
                "EndPointServiceId": "vpcsvc-prvrnrlt",
                "EndPointVipSet": [
                    "10.0.0.17:53"
                ],
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ]
            }
        ]
    }
}
```

