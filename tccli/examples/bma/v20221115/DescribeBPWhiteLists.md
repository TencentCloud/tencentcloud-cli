**Example 1: 查询白名单列表**

查询白名单列表

Input: 

```
tccli bma DescribeBPWhiteLists --cli-unfold-argument  \
    --Filters.0.Name CompanyId \
    --Filters.0.Value 123 \
    --Filters.1.Name AssetsType \
    --Filters.1.Value 0 \
    --Filters.2.Name WhiteList \
    --Filters.2.Value 白名单名称 \
    --Filters.3.Name StartTime \
    --Filters.3.Value 2022-10-01 00:00:00 \
    --Filters.4.Name EndTime \
    --Filters.4.Value 2022-10-01 23:59:59 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "WhiteLists": [
            {
                "WhiteListId": 123,
                "CompanyId": 123,
                "BrandName": "品牌名称",
                "AssetsType": 0,
                "WhiteList": "白名单名称",
                "InsertTime": "2022-10-01 00:00:00"
            }
        ],
        "TotalCount": 10,
        "RequestId": "xxx"
    }
}
```

