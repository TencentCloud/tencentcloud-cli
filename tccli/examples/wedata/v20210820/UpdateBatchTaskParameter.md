**Example 1: 批量修改Dlc参数**

批量修改Dlc参数

Input: 

```
tccli wedata UpdateBatchTaskParameter --cli-unfold-argument  \
    --TaskIds 20230510112238320 \
    --DlcParameterInfo.DriverSize small \
    --DlcParameterInfo.ExecutorMaxNumbers 4 \
    --DlcParameterInfo.ExecutorNumbers 4 \
    --DlcParameterInfo.ExecutorSize 1 \
    --DlcParameterInfo.RunConfParams dasdasaaaaaaaaaaaaa
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "TotalNumber": 1,
        "SuccessNumber": 1,
        "FailNumber": 0
    }
}
```

**Example 2: 批量修改TCHouse-X任务参数**



Input: 

```
tccli wedata UpdateBatchTaskParameter --cli-unfold-argument  \
    --TaskIds abc \
    --ProjectId abc \
    --TCHouseXTaskParameter.DriverCores 0 \
    --TCHouseXTaskParameter.ExecutorCores 0 \
    --TCHouseXTaskParameter.NumExecutors 0
```

Output: 
```
{
    "Response": {
        "TotalNumber": 1,
        "SuccessNumber": 1,
        "FailNumber": 1,
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

