**Example 1: 查询dspm数据识别分类列表**



Input: 

```
tccli csip DescribeDspmIdentifyCategoryList --cli-unfold-argument  \
    --MemberId mem-12jnednj \
    --Filter.Limit 10 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Id": 359,
                "Name": "自定义分类",
                "Type": 1,
                "UpdateTime": "2026-04-27 17:00:32"
            }
        ],
        "TotalCount": 1,
        "RequestId": "b4d5f13f-43a0-4723-8ca9-ab768087c2f7"
    }
}
```

