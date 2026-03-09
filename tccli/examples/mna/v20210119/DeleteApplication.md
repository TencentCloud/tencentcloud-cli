**Example 1: 删除应用**



Input: 

```
tccli mna DeleteApplication --cli-unfold-argument  \
    --MpApplicationIdList.0.MpApplicationId test1 \
    --MpApplicationIdList.1.MpApplicationId test2
```

Output: 
```
{
    "Response": {
        "RequestId": "527cc5c7-0413-33e9-2adc-632e0f6a9dff"
    }
}
```

