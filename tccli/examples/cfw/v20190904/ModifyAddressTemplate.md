**Example 1: 修改地址模板**



Input: 

```
tccli cfw ModifyAddressTemplate --cli-unfold-argument  \
    --Uuid abc \
    --Name abc \
    --Detail abc \
    --IpString abc \
    --Type 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Uuid": "abc",
        "RequestId": "abc"
    }
}
```

