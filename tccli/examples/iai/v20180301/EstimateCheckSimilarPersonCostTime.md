**Example 1: 获取人员查重预估需要时间接口调用成功**



Input: 

```
tccli iai EstimateCheckSimilarPersonCostTime --cli-unfold-argument  \
    --GroupIds MyGroup1 MyGroup2
```

Output: 
```
{
    "Response": {
        "EstimatedTimeCost": 1,
        "RequestId": "14252604-a4ce-432e-9cb3-4ca15bf88e0d"
    }
}
```

**Example 2: 获取人员查重预估需要时间接口调用失败**



Input: 

```
tccli iai EstimateCheckSimilarPersonCostTime --cli-unfold-argument  \
    --GroupIds AAAAAAA bbbbbbb
```

Output: 
```
{
    "Response": {
        "RequestId": "b590639d-b84f-4821-9d53-bc7351daf5d0"
    }
}
```

