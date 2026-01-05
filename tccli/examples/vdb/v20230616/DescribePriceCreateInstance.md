**Example 1: 成功**



Input: 

```
tccli vdb DescribePriceCreateInstance --cli-unfold-argument  \
    --ProductType 0 \
    --InstanceType single \
    --Mode single \
    --Cpu 4 \
    --Memory 8 \
    --DiskSize 50 \
    --WorkerNodeNum 3 \
    --PayMode 1 \
    --PayPeriod 1 \
    --GoodsNum 1
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "OriginalPrice": 226200,
        "Price": 78360,
        "RequestId": "3558ca88-aa24-4573-b802-ec2516096fd7"
    }
}
```

