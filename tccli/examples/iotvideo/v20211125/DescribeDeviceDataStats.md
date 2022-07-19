**Example 1: 查询设备数据统计**



Input: 

```
tccli iotvideo DescribeDeviceDataStats --cli-unfold-argument  \
    --StartDate 2022-06-11 \
    --EndDate 2022-06-13 \
    --ProductId L78xxxxZ95
```

Output: 
```
{
    "Response": {
        "RequestId": "4b658399-9313-4d92-8b0c-458c7765a0b6",
        "RegisterCnt": 15,
        "Data": [
            {
                "Date": "2022-06-11",
                "NewRegisterCnt": 0,
                "NewActivateCnt": 0,
                "ActiveCnt": 0
            },
            {
                "Date": "2022-06-12",
                "NewRegisterCnt": 0,
                "NewActivateCnt": 0,
                "ActiveCnt": 0
            },
            {
                "Date": "2022-06-13",
                "NewRegisterCnt": 0,
                "NewActivateCnt": 0,
                "ActiveCnt": 0
            }
        ],
        "Total": 3
    }
}
```

