**Example 1: 添加阻断白名单列表**



Input: 

```
tccli cwp CreateBanWhiteList --cli-unfold-argument  \
    --Rules.Remark 备注 \
    --Rules.Uuid 05f0bcab-726c-4ea4-8109-bcd03d5598f7 \
    --Rules.IsGlobal True \
    --Rules.Id 1 \
    --Rules.ModifyTime 2020-09-22 00:00:00 \
    --Rules.SrcIp 1.1.1.1 \
    --Rules.CreateTime 2020-09-22 00:00:00 \
    --Rules.Quuids 05f0bcab-726c-4ea4-8109-bcd03d5598f7
```

Output: 
```
{
    "Response": {
        "IsDuplicate": true,
        "IsGlobal": false,
        "DuplicateHosts": [
            {
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Id": 1
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

