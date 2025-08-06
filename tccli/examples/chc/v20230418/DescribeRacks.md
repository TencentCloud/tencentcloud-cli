**Example 1: 获取机架列表**



Input: 

```
tccli chc DescribeRacks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RackSet": [
            {
                "HostingType": "客户独享",
                "IdcId": 159,
                "IdcName": "天津数据备份中心东区DC",
                "IdcUnitId": 568,
                "IdcUnitName": "天津数据备份中心东区DC1栋M301",
                "IsPowerOn": true,
                "RackId": 15082,
                "RackName": "M301-E10",
                "RackOpenTime": "2021-09-06"
            }
        ],
        "RequestId": "4df8264f-8348-4e02-98d3-bb4e85c651be",
        "Total": 2217
    }
}
```

