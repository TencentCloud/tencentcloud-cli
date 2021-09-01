**Example 1: 查询物联网卡详情信息**



Input: 

```
tccli ic DescribeApp --cli-unfold-argument  \
    --Sdkappid 1200168178
```

Output: 
```
{
    "Response": {
        "RequestId": "124145i30913",
        "Data": {
            "Sdkappid": "1400168178",
            "Appkey": "20676074e3db4492efb0471b4cbec2f1",
            "CloudAppid": "1256872341",
            "Name": "test",
            "Description": "descr",
            "CreatedTime": "2018-12-11 15:40:01",
            "BizType": 1,
            "Uin": "100008340870"
        }
    }
}
```

