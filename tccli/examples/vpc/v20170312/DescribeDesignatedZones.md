**Example 1: 查询用户当前地域可选的特殊可用区**



Input: 

```
tccli vpc DescribeDesignatedZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DesignatedZoneInfo": [
            {
                "DesignatedZone": "ap-guangzhou-tez-guangzhou-1",
                "DesignatedZoneName": "广州边缘一区",
                "DesignatedZoneType": "TEZ"
            }
        ],
        "TotalCount": 1,
        "RequestId": "aa04ac3c-f3c8-410e-8c59-9ab30c032604"
    }
}
```

