**Example 1: ReceiveAiNotice**



Input: 

```
tccli taop ReceiveAIRunNotice --cli-unfold-argument  \
    --Src 1 \
    --Code 0 \
    --Mem 0 \
    --GpuNum 0 \
    --BucketName taop-251199828-251010749 \
    --TaskId uoio-dkjfksa-dkfna-nddj \
    --Msg success \
    --Path /data/test.csv \
    --EndTime 2021-07-12 10:48:00 \
    --GpuType TI.8XLARGE64.32core64g \
    --BeginTime 2021-07-12 10:45:00
```

Output: 
```
{
    "Response": {
        "RequestId": "4a1cb6bb-92d3-48fa-8d5d-b4dcd636868f",
        "Result": "success"
    }
}
```

