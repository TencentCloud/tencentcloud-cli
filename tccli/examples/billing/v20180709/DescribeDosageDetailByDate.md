**Example 1: 互动直播、CDN业务按日期获取用量明细**

互动直播、CDN业务按日期获取用量明细

Input: 

```
tccli billing DescribeDosageDetailByDate --cli-unfold-argument  \
    --StartDate 2019-01-01 \
    --Domain www.gdxxb.com \
    --EndDate 2019-01-01 \
    --ProductCode 10181
```

Output: 
```
{
    "Response": {
        "RetCode": 0,
        "RetMsg": "",
        "Unit": "bps",
        "DetailSets": [
            {
                "Domain": "ddfs.dfwfn2.cn",
                "InstanceID": "ddfs.dfwfn2.cn",
                "DetailPoints": [
                    {
                        "Time": "2019-01-01 00:00:00",
                        "Value": "18731317843"
                    }
                ]
            }
        ],
        "RequestId": "f4fbb2f0-d93b-4828-a156-79a43f29da6d"
    }
}
```

**Example 2: CLB、EIP，视频直播业务按日期获取用量明细**

CLB、EIP，视频直播业务按日期获取用量明细

Input: 

```
tccli billing DescribeDosageDetailByDate --cli-unfold-argument  \
    --StartDate 2019-01-01 \
    --Domain  "" \
    --EndDate 2019-01-01 \
    --ProductCode 10181
```

Output: 
```
{
    "Response": {
        "RetCode": 0,
        "RetMsg": "",
        "Unit": "GB",
        "DetailSets": [
            {
                "Domain": "",
                "InstanceID": "lb-1zvuxyml",
                "DetailPoints": [
                    {
                        "Time": "2019-01-01 00:00:00",
                        "Value": "18731317843"
                    }
                ]
            }
        ],
        "RequestId": "f4fbb2f0-d93b-4828-a156-79a43f29da6d"
    }
}
```

