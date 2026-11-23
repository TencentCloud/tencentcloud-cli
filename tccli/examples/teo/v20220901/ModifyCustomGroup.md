**Example 1: 修改 TLS 指纹组内容**

已有一个 TLS 指纹组，向其中追加一个 JA4 值。

Input: 

```
tccli teo ModifyCustomGroup --cli-unfold-argument  \
    --ZoneId zone-3nw1o2owaf7p \
    --GroupId 273746923 \
    --GroupItemOperation Append \
    --GroupItems.0.Content t13d1812h2_e8a523a41297_ef7df7f74e48 \
    --GroupItems.0.ItemType JA4
```

Output: 
```
{
    "Response": {
        "RequestId": "3296318f-6aad-461f-84de-85805697a75e"
    }
}
```

