**Example 1: 修改水印密钥**



Input: 

```
tccli dayu ModifyDDoSWaterKey --cli-unfold-argument  \
    --Business bgpip \
    --PolicyId policy-000000xe \
    --Method add \
    --KeyId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "KeyList": [
            {
                "KeyId": 1234,
                "KeyContent": "abc6b301-a322-493a-8e36-83b295453497",
                "KeyVersion": "123",
                "OpenStatus": 1,
                "CreateTime": "2019-11-21 11:00:00"
            }
        ]
    }
}
```

