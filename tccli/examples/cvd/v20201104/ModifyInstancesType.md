**Example 1: 后付费变配示例**



Input: 

```
tccli cvd ModifyInstancesType --cli-unfold-argument  \
    --InstanceIds cdi-krxgg2id76erx4f cdi-hd1vj94so0f5eju \
    --InstanceType S1L.LARGE16 \
    --ChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "RequestId": "d2afb2d3-e969-457a-b21b-417827b9b56f"
    }
}
```

**Example 2: 预付费变配示例**



Input: 

```
tccli cvd ModifyInstancesType --cli-unfold-argument  \
    --InstanceIds cdi-k7ay0fg1oru3zoa cdi-p1xzld22kkvwmoj \
    --InstanceType S3L.2XLARGE16 \
    --ChargeType PREPAID
```

Output: 
```
{
    "Response": {
        "RequestId": "a22a66f9-21c5-47f7-a7e0-9ff40e6daa9d"
    }
}
```

