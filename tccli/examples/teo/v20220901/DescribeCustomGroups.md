**Example 1: 查询站点下所有自定义组**

查询指定站点下所有自定义组内容。

Input: 

```
tccli teo DescribeCustomGroups --cli-unfold-argument  \
    --ZoneId zone-3nw1o2owaf7p
```

Output: 
```
{
    "Response": {
        "CustomGroups": [
            {
                "GroupId": "273746923",
                "GroupItemTotalCount": 2,
                "GroupItems": [
                    {
                        "Content": "080376eff4b9c0bb02f14d42705994be",
                        "ItemType": "JA3"
                    }
                ],
                "GroupName": "tls_group_1",
                "GroupType": "TLSFingerprint"
            }
        ],
        "GroupTotalCount": 1,
        "RequestId": "266b1419-4bd5-44d1-8be2-c31806539d6e"
    }
}
```

