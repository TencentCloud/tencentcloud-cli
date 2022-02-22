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
        "RequestId": "5facf6b3-9bd5-480b-98c9-51d7285cf064",
        "Data": {
            "Sdkappid": "1200168178",
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

