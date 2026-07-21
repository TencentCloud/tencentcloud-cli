**Example 1: 查询防火墙支持的地域规则列表**



Input: 

```
tccli cfw DescribeAclRegInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Area": 0,
                "EnKey": "H",
                "ForBypass": 1,
                "ForNat": 1,
                "ForSerial": 1,
                "IsCity": 1,
                "Num": 0,
                "Parent": "R_MAINLAND",
                "RegionCode": "hb13",
                "RegionName": "河北省",
                "ZhKey": "H"
            }
        ],
        "RequestId": "0203ad2c-fc57-4d7c-9858-4c3d7e650d28"
    }
}
```

