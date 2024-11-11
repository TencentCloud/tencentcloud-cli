**Example 1: 创建数据建模示例**

创建数据建模示例，实现数据建模的下单支付及发货

Input: 

```
tccli wedata CreateDataModel --cli-unfold-argument  \
    --CloudappId cloudapp-x3hadra3jjj \
    --TimeUnit m \
    --TimeSpan 1 \
    --AutoRenewFlag 0 \
    --DataModelVersion DATA_MODEL_STANDARD \
    --UserId 10002855
```

Output: 
```
{
    "RequestId": "a4f6d342-5bc5-47f0-a378-3b6aa993a576",
    "Response": {
        "Data": "fd91ff2e-ea72-414a-8772-6edaa61a07f6",
        "RequestId": "a4f6d342-5bc5-47f0-a378-3b6aa993a576"
    }
}
```

