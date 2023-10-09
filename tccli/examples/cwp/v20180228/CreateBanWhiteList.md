**Example 1: 添加阻断白名单列表**



Input: 

```
tccli cwp CreateBanWhiteList --cli-unfold-argument  \
    --Rules.Remark xx \
    --Rules.Uuid xx \
    --Rules.IsGlobal True \
    --Rules.Id xx \
    --Rules.ModifyTime 2020-09-22 00:00:00 \
    --Rules.SrcIp xx \
    --Rules.CreateTime 2020-09-22 00:00:00 \
    --Rules.Quuids xx
```

Output: 
```
{
    "Response": {
        "IsDuplicate": true,
        "IsGlobal": false,
        "DuplicateHosts": [
            {
                "Quuid": "xx",
                "Uuid": "xx",
                "Id": 1
            },
            {
                "Id": 1,
                "Quuid": "xx",
                "Uuid": "xx"
            },
            {
                "Id": 1,
                "Quuid": "xx",
                "Uuid": "xx"
            },
            {
                "Id": 1,
                "Quuid": "xx",
                "Uuid": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

