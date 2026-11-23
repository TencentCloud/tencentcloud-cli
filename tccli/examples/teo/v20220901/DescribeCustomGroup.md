**Example 1: 查询自定义组内容**

查询指定自定义组详细内容。

Input: 

```
tccli teo DescribeCustomGroup --cli-unfold-argument  \
    --ZoneId zone-3nw1o2owaf7p \
    --GroupId 273746923
```

Output: 
```
{
    "Response": {
        "GroupId": "273746923",
        "GroupItemTotalCount": 1,
        "GroupItems": [
            {
                "Content": "080376eff4b9c0bb02f14d42705994be",
                "ItemType": "JA3"
            }
        ],
        "GroupName": "tls_group_1",
        "GroupType": "TLSFingerprint",
        "RequestId": "772aa1f5-5c3f-41b1-b638-b6ecfd0fc135"
    }
}
```

