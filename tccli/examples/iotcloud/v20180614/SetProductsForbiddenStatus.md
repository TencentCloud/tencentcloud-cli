**Example 1: 批量设置产品禁用状态**



Input: 

```
tccli iotcloud SetProductsForbiddenStatus --cli-unfold-argument  \
    --ProductID productID1 productID2 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

