**Example 1: 获取用量明细数据**

获取用量明细数据

Input: 

```
tccli billing DescribeDosageDetailList --cli-unfold-argument  \
    --Offset 43150 \
    --Limit 3 \
    --StartTime 2023-09-01 \
    --EndTime 2023-09-30 \
    --ProductCode p_dsa
```

Output: 
```
{
    "Response": {
        "Record": [
            {
                "AttrStr": [
                    {
                        "Key": "zoneId",
                        "Value": "470004"
                    },
                    {
                        "Key": "dayPeek",
                        "Value": "4872430721"
                    },
                    {
                        "Key": "regionId",
                        "Value": "47"
                    }
                ],
                "BillingItemCode": "v_dsa_gipa_bandwidth_game",
                "BillingItemCodeName": "全球IP应用加速-游戏加速带宽",
                "Date": "2023-09-01",
                "DeductValue": 0,
                "DosageBeginTime": "2023-09-01 00:02:00",
                "DosageEndTime": "2023-09-01 00:02:59",
                "DosageType": "minute",
                "DosageUnit": "Mbps",
                "DosageValue": 2206972795,
                "ProductCode": "p_dsa",
                "ProductCodeName": "全站加速网络ECDN",
                "RemainValue": 2206972795,
                "SdkAppId": "",
                "SheetName": [
                    "全球IP应用加速_1分钟"
                ],
                "SubBillingItemCode": "sv_dsa_gipa_bandwidth_game_yd_month",
                "SubBillingItemCodeName": "GIPA-游戏加速带宽-移动网络-按月结算",
                "SubProductCode": "sp_dsa_gipa",
                "SubProductCodeName": "全球IP应用加速",
                "Uin": "909619400"
            }
        ],
        "RequestId": "184cd45e-d2e1-4043-a47b-183617836e25"
    }
}
```

