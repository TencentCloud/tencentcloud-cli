**Example 1: 查询活动列表**



Input: 

```
tccli wav QueryActivityList --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "jQ+8f/xhRbMzAxSUUgYbgiYY28BzY+xFM6JuYjezhUQ=",
        "PageData": [
            {
                "ActivityState": 20,
                "ActivityName": "新建打圈互动111",
                "EndTime": 1627022340,
                "ActivityId": 1407589595607994444,
                "UpdateTime": 1624430486,
                "StartTime": 1624377600,
                "ActivityType": 101,
                "PrivacyAgreementId": "",
                "MainPhoto": "https://tmap-travel-didi-1255598736.cos.ap-guangzhou.myqcloud.com/media/92d8452b-e194-4d59-a28e-7300d0556976.jpg",
                "ActivityDataList": "{\"couponTypeList\":[1],\"couponInfoList\":[{\"couponId\":\"C1407254077494390786\",\"couponName\":\"自动化创建满减券161480\",\"thresholdAmount\":15000000,\"discountAmount\":15000000,\"discountPercentage\":0,\"couponType\":1,\"availableTimeType\":1,\"availableBeginTime\":0,\"availableEndTime\":10368000}]}"
            }
        ],
        "RequestId": "d143e1fc-1106-4b3e-a9cd-854b09b51752"
    }
}
```

