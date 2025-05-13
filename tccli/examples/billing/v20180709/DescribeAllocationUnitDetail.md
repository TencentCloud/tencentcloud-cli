**Example 1: 查询分账单元详情**



Input: 

```
tccli billing DescribeAllocationUnitDetail --cli-unfold-argument  \
    --Id 6 \
    --Month 2022-10-01
```

Output: 
```
{
    "Response": {
        "Id": 6,
        "Uin": "909619400",
        "Name": "产品一部",
        "ParentId": 4,
        "SourceName": "一组",
        "SourceId": "asd221",
        "Remark": "备注1",
        "TreeNodeUniqKey": "909619400-6358ee8995950",
        "RuleId": 23,
        "RequestId": "e93a707c-f31f-417f-a39b-e72380132dbb"
    }
}
```

