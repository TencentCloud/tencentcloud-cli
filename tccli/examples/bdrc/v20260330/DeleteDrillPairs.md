**Example 1: 删除演练**



Input: 

```
tccli bdrc DeleteDrillPairs --cli-unfold-argument  \
    --DrillPairType INSTANCE \
    --DrillPairIds drillpair-2zjmpdlb \
    --DrillGroupIds dg-2zjmpdlb \
    --DeleteDrillResource True
```

Output: 
```
{
    "Response": {
        "DeleteDrillPairGroupSet": [
            "dg-2zjmpdlb"
        ],
        "DeleteDrillPairResultSet": [
            {
                "Code": "Success",
                "DrillPairId": "drillpair-2zjmpdlb",
                "Message": ""
            }
        ],
        "RequestId": "c60affa9-8642-4265-8a87-8ac8c496f480"
    }
}
```

