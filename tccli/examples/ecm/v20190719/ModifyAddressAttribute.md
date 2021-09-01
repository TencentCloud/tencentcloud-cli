**Example 1: 修改EIP名称**



Input: 

```
tccli ecm ModifyAddressAttribute --cli-unfold-argument  \
    --AddressId eip-11112222 \
    --AddressName test_eip \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

**Example 2: 修改EIP 直通属性**



Input: 

```
tccli ecm ModifyAddressAttribute --cli-unfold-argument  \
    --AddressId eip-11112222 \
    --EipDirectConnection FALSE \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "RequestId": "ABCD0BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

