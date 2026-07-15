**Example 1: 查询视频理解后付费用量曲线**



Input: 

```
tccli iotexplorer DescribeTWeSeeTaskStatistics --cli-unfold-argument  \
    --ServiceType VID_COMP \
    --ServiceTier POSTPAID \
    --StartTime 1776621600 \
    --EndTime 1776625200 \
    --Interval 3600
```

Output: 
```
{
    "Response": {
        "StatData": [
            {
                "CostAdvanced": 1,
                "CostBasic": 2,
                "Count": 2,
                "Time": "2026-04-20 02:00:00"
            }
        ],
        "RequestId": "1748dfa6-9e11-4ec7-a782-4393d58665e2"
    }
}
```

**Example 2: 查询视频理解包年包月基础版用量曲线**



Input: 

```
tccli iotexplorer DescribeTWeSeeTaskStatistics --cli-unfold-argument  \
    --ServiceType VID_COMP \
    --ServiceTier BASIC \
    --StartTime 1776621600 \
    --EndTime 1776625200 \
    --Interval 3600
```

Output: 
```
{
    "Response": {
        "StatData": [
            {
                "CostAdvanced": 0,
                "CostBasic": 0,
                "Count": 0,
                "Time": "2026-04-20 02:00:00"
            }
        ],
        "RequestId": "72161955-e6b9-4f31-8e2f-f54980fae9d5"
    }
}
```

