**Example 1: 批量解绑子产品**



Input: 

```
tccli iotexplorer UnbindProducts --cli-unfold-argument  \
    --GatewayProductId 89FEGTES8 \
    --ProductIds UJ8HE90G
```

Output: 
```
{
    "Response": {
        "GatewayDeviceNames": [
            "gateway_test1"
        ],
        "RequestId": "32150866-743e-4a1b-ade5-c690ac2cc0b5"
    }
}
```

