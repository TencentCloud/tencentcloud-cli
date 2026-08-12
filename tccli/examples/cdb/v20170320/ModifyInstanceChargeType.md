**Example 1: 修改实例的计费模式**

包年包月转为按量计费

Input: 

```
tccli cdb ModifyInstanceChargeType --cli-unfold-argument  \
    --InstanceId cdb-3sism8n9 \
    --InstanceChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "DealName": "20260226228022238944971",
        "RequestId": "fd2d4e79-61ff-421f-b6d5-fa28225a7ee6"
    }
}
```

