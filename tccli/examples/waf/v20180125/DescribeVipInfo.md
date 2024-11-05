**Example 1: 查询vip**

查询实例的vip信息

Input: 

```
tccli waf DescribeVipInfo --cli-unfold-argument  \
    --InstanceIds waf_7j8fsghd0080b
```

Output: 
```
{
    "Response": {
        "RequestId": "31fc0e49-7472-4ee4-a1a1-391b96119c7e",
        "VipInfo": [
            {
                "Vip": "120.23.93.35",
                "InstanceId": "waf_7j8fsghd0080b",
                "InstanceCreateTime": "2020-08-19T14:41:10+08:00",
                "Region": "ap-beijing",
                "RegionId": 8,
                "ISP": "BGP",
                "VipType": "ipv4",
                "AddressName": "fa44989badbc9e09-cl2.qcloudwzgj.com"
            }
        ]
    }
}
```

