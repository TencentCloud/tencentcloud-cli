**Example 1: 查询片区**



Input: 

```
tccli rum DescribeTawAreas --cli-unfold-argument  \
    --AreaIds 1 \
    --AreaStatuses 1 \
    --Limit 0 \
    --Offset 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AreaSet": [
            {
                "AreaId": 1,
                "AreaStatus": 1,
                "AreaName": "中国大陆",
                "AreaKey": "area_cn_dl"
            }
        ],
        "RequestId": "10f605a3-6480-4254-bbb7-7ca1ab6a133e"
    }
}
```

