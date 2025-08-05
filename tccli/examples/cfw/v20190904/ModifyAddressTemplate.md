**Example 1: 修改地址模板**



Input: 

```
tccli cfw ModifyAddressTemplate --cli-unfold-argument  \
    --Name 放通ip \
    --Detail 放通ip \
    --IpString 1.1.1.1 \
    --Type 1 \
    --ProtocolType 4 \
    --Uuid mb_appid_1708504391199
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RuleLimitNum": 3000,
        "Uuid": "mb_appid_1708504391199",
        "RequestId": "RequestId"
    }
}
```

