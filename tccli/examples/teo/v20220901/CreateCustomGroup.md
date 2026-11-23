**Example 1: 创建 TLS 指纹组**

创建一个 TLS 指纹组，并添加一个 JA3 值。

Input: 

```
tccli teo CreateCustomGroup --cli-unfold-argument  \
    --ZoneId zone-3nw1o2owaf7p \
    --GroupName tls_group_1 \
    --GroupType TLSFingerprint \
    --GroupItems.0.Content 080376eff4b9c0bb02f14d42705994be \
    --GroupItems.0.ItemType JA3
```

Output: 
```
{
    "Response": {
        "GroupId": "273746923",
        "GroupItems": [
            {
                "Content": "080376eff4b9c0bb02f14d42705994be",
                "ItemType": "JA3"
            }
        ],
        "GroupName": "tls_group_1",
        "GroupType": "TLSFingerprint",
        "RequestId": "eaadf524-d010-4ecb-9915-b6633b8230ed"
    }
}
```

