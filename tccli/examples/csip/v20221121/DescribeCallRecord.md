**Example 1: 示例1**



Input: 

```
tccli csip DescribeCallRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessKey": "AKID******",
                "AccessKeyID": 10022,
                "AccessKeyRemark": "",
                "AppID": 100001,
                "CallCount": 241,
                "CallID": "202528000005473835",
                "Code": 0,
                "Date": "2025-07-11 00:00:00",
                "EventName": "GetFederationToken",
                "EventType": 1,
                "FirstCallTime": "2025-07-11 00:00:00",
                "IPType": 3,
                "ISP": "腾讯云",
                "InstanceID": "",
                "InstanceName": "",
                "LastCallTime": "2025-07-11 14:19:00",
                "PolicySet": [
                    "default-policy"
                ],
                "ProductName": "sts",
                "Region": "中国-广东省-广州市",
                "ShowStatus": true,
                "SourceIP": "106.55.123.**",
                "SourceIPRemark": "remark",
                "UserName": "name",
                "UserType": "CAMUser"
            }
        ],
        "Total": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

