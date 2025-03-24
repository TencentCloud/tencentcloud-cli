**Example 1: 请求示例**



Input: 

```
tccli chc DescribeIdcs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IdcSet": [
            {
                "IdcId": 373,
                "IdcName": "天津数据备份中心东区3栋DC",
                "IdcUnitSet": [
                    {
                        "CageSet": [
                            {
                                "CageName": "cage2",
                                "CheckerSet": []
                            }
                        ],
                        "IdcUnitId": 2555,
                        "IdcUnitName": "天津数据备份中心东区3栋DCM202"
                    }
                ]
            }
        ],
        "RequestId": "b8211320-9409-4ec7-b75f-11674b2bc9fc"
    }
}
```

