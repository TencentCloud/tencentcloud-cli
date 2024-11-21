**Example 1: 开关列表枚举**

开关列表枚举

Input: 

```
tccli cfw DescribeSwitchLists --cli-unfold-argument  \
    --Status 0 \
    --Type CVM \
    --Area 成都 \
    --SearchValue {"common":"1.14.67.183"} \
    --Limit 1 \
    --Offset 0 \
    --Order asc \
    --By PortTimes
```

Output: 
```
{
    "Response": {
        "AreaLists": [
            "上海",
            "重庆",
            "深圳金融",
            "成都",
            "广州",
            "北京"
        ],
        "Data": [
            {
                "Area": "成都",
                "AssetType": "CVM",
                "Id": 6414090,
                "InstanceId": "ins-fdysvd0j",
                "InstanceName": "nta-服务端性能",
                "IntranetIp": "10.26.26.11,10.26.26.15,10.26.26.30,10.26.26.31,10.26.26.32,10.26.26.33,10.26.26.34,10.26.26.35,10.26.26.36,10.26.26.37",
                "LastTime": "2024-03-08 14:56:54",
                "PortTimes": 0,
                "PublicIp": "1.14.67.183",
                "PublicIpType": 2,
                "ScanMode": "light",
                "ScanStatus": 0,
                "Switch": 0
            }
        ],
        "OffNum": 30,
        "OnNum": 1,
        "RequestId": "acdf46bf-c640-4946-9740-1fde401b9b60",
        "Total": 1
    }
}
```

