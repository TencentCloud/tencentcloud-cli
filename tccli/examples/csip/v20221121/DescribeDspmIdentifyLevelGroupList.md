**Example 1: 查询dspm数据识别分级组列表**



Input: 

```
tccli csip DescribeDspmIdentifyLevelGroupList --cli-unfold-argument  \
    --MemberId mem-123edwq9 \
    --Filter.Limit 10 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Description": "级别描述",
                "Id": 7,
                "LevelItems": [
                    {
                        "LevelId": 18,
                        "LevelName": "高",
                        "LevelScore": 10
                    }
                ],
                "Name": "自定义级别03",
                "Type": 1,
                "UpdateTime": "2026-04-28 17:57:13"
            }
        ],
        "TotalCount": 3,
        "RequestId": "d7049b2d-c3e1-4952-8616-d7e09dbcdf78"
    }
}
```

