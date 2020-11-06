**Example 1: Querying the price of scale-out**



Input: 

```
tccli emr InquiryPriceScaleOutInstance --cli-unfold-argument  \
    --TimeUnit s \
    --TimeSpan 3600 \
    --ZoneId 100003 \
    --PayMode 0 \
    --InstanceId emr-3ida6zmi \
    --CoreCount 1 \
    --TaskCount 0 \
    --Currency CNY \
    --RouterCount 0
```

Output: 
```
{
    "Response": {
        "RequestId": "04daa603-e1e7-4243-b25d-31e6a6736528"
    }
}
```

