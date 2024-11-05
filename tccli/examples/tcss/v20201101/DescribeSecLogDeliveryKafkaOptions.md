**Example 1: 查询安全日志投递kafka可选项**



Input: 

```
tccli tcss DescribeSecLogDeliveryKafkaOptions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceList": [],
        "RegionList": [
            {
                "Region": "ap-bangkok",
                "RegionName": "亚太东南(曼谷)"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "华北地区(北京)"
            },
            {
                "Region": "ap-beijing-fsi",
                "RegionName": "华北地区(北京金融)"
            },
            {
                "Region": "ap-changsha-ec",
                "RegionName": "华中地区(长沙ec)"
            },
            {
                "Region": "ap-chengdu",
                "RegionName": "西南地区(成都)"
            },
            {
                "Region": "ap-chongqing",
                "RegionName": "西南地区(重庆)"
            }
        ],
        "RequestId": "a9761df9-00d1-4102-8176-0c9be0e11c59"
    }
}
```

