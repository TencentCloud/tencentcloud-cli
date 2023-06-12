**Example 1: 查询实例的售卖价格**

查询实例的售卖价格

Input: 

```
tccli postgres InquiryPriceCreateDBInstances --cli-unfold-argument  \
    --InstanceCount 1 \
    --Zone ap-guangzhou-2 \
    --Storage 100 \
    --Pid 11004 \
    --Period 1 \
    --SpecCode cdb.pg.z1.2g \
    --InstanceChargeType PREPAID
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab",
        "OriginalPrice": 27600,
        "Price": 27600,
        "Currency": "CNY"
    }
}
```

