**Example 1: 查询接口**



Input: 

```
tccli vpc DescribeCcnRouteTables --cli-unfold-argument  \
    --Filters.0.Name route-table-id \
    --Filters.0.Values ccnrtb-mnvhfmv9 ccnrtb-3230jx4x \
    --Filters.1.Name route-table-name \
    --Filters.1.Values _default_rtb rubytest \
    --Filters.2.Name ccn-id \
    --Filters.2.Values ccn-8j0phqix
```

Output: 
```
{
    "Response": {
        "CcnRouteTableSet": [
            {
                "CcnId": "ccn-8j0phqix",
                "CcnRouteTableId": "ccnrtb-mnvhfmv9",
                "RouteTableName": "_default_rtb",
                "RouteTableDescription": "table-1",
                "IsDefaultTable": true,
                "CreateTime": "2021-05-11 15:47:53"
            },
            {
                "CcnId": "ccn-8j0phqix",
                "CcnRouteTableId": "ccnrtb-3230jx4x",
                "RouteTableName": "rubytest",
                "RouteTableDescription": "table-2",
                "IsDefaultTable": false,
                "CreateTime": "2021-05-11 16:33:14"
            }
        ],
        "TotalCount": 2,
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

