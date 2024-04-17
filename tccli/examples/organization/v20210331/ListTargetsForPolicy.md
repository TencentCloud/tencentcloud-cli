**Example 1: 查询某个指定策略关联的目标列表**

查询某个指定策略关联的目标列表

Input: 

```
tccli organization ListTargetsForPolicy --cli-unfold-argument  \
    --PolicyId 134173928
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AddTime": "2022-08-09 17:08:35",
                "Name": "T0",
                "RelatedType": 1,
                "Uin": 222222222222
            },
            {
                "AddTime": "2022-08-09 17:11:54",
                "Name": "33",
                "RelatedType": 2,
                "Uin": 111111111111
            }
        ],
        "RequestId": "676ed1a2-8a98-4834-8d7a-19538980ad0e",
        "TotalNum": 5
    }
}
```

