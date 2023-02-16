**Example 1: 查询白名单列表**

查询白名单列表

Input: 

```
tccli bma DescribeBPWhiteLists --cli-unfold-argument ```

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

