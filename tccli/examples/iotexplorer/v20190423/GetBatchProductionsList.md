**Example 1: 列出量产数据列表**



Input: 

```
tccli iotexplorer GetBatchProductionsList --cli-unfold-argument  \
    --ProjectId prj-pq00mstg \
    --Offset 0 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "BatchProductions": [
            {
                "BatchProductionId": "LC-7n72wlih",
                "ProductId": "R32ONVL0EU",
                "ProductName": "test1",
                "BurnMethod": 0,
                "CreateTime": 1574758357
            }
        ],
        "RequestId": "rest-client230191026",
        "TotalCnt": 1
    }
}
```

