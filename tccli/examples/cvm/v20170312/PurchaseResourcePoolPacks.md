**Example 1: 创建实例资源池预扣包**

创建一个实例资源池预扣包

Input: 

```
tccli cvm PurchaseResourcePoolPacks --cli-unfold-argument  \
    --Zone ap-guangzhou-7 \
    --InstanceType S9.8XLARGE64 \
    --InstanceCount 1 \
    --Period 1
```

Output: 
```
{
    "Response": {
        "DedicatedResourcePackIdSet": [
            "rpp-2gyonkx7"
        ],
        "RequestId": "b0c7e70b-c576-40d7-b2fd-1807a7400616"
    }
}
```

