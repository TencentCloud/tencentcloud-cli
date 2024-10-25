**Example 1: 修改地址模板**



Input: 

```
tccli cfw ModifyAddressTemplate --cli-unfold-argument  \
    --Name dora \
    --Detail  \
    --IpString 1.1.1.1 \
    --Type 1 \
    --ProtocolType  \
    --Uuid mb_appid_1708504391199
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Uuid": "mb_appid_1708504391199",
        "RequestId": "RequestId"
    }
}
```

