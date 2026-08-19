**Example 1: 示例**

查询订单列表

Input: 

```
tccli csip DescribeCWPOrderList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Alias": "",
                "AutoRenewFlag": 0,
                "BeginTime": "2026-03-03 16:51:53",
                "DealName": "",
                "EndTime": "2026-03-10 16:51:53",
                "ExtraParam": {
                    "DisposableStatus": false,
                    "Mode": "PrePay"
                },
                "InquireKey": "sv_yunjing_ue_aams",
                "InquireNum": 10,
                "PayMode": 1,
                "ProductCode": "p_yunjing",
                "ProjectID": 0,
                "RegionID": 1,
                "ResourceId": "white_e141179b8afc4ca4af029791f9dd6008",
                "SourceType": 6,
                "Status": 3,
                "SubProductCode": "sp_yunjing_0014552",
                "TagList": [],
                "UsedNum": 0,
                "ZoneID": 100001
            }
        ],
        "TotalCount": 1,
        "RequestId": "25203ee3-1f33-432d-8c24-96bc8ab92316"
    }
}
```

