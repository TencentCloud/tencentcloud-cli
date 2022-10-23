**Example 1: 策略列表**



Input: 

```
tccli cwp DescribeBaselinePolicyList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PolicyName": "未授权访问",
                "DetectInterval": 1,
                "DetectTime": "17:00:00",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    70,
                    71,
                    72,
                    73,
                    74,
                    75,
                    76
                ],
                "HostIds": [],
                "HostIps": [],
                "PolicyId": 63,
                "RuleCount": 7,
                "ItemCount": 7,
                "HostCount": 8,
                "IsDefault": 1
            },
            {
                "PolicyName": "腾讯安全标准",
                "DetectInterval": 1,
                "DetectTime": "17:00:00",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    120,
                    121,
                    122,
                    123,
                    124,
                    125
                ],
                "HostIds": [],
                "HostIps": [],
                "PolicyId": 64,
                "RuleCount": 6,
                "ItemCount": 35,
                "HostCount": 8,
                "IsDefault": 1
            },
            {
                "PolicyName": "29sjjsjsdk529ssj1kckdkckjssioe0e9diceivffffjfffjfffi29495888529sjjsjsdkckdkckjssioe0e9diceivffffjfffjfffi294958885",
                "DetectInterval": 1,
                "DetectTime": "09:35:30",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    11
                ],
                "HostIds": [],
                "HostIps": [
                    ""
                ],
                "PolicyId": 136,
                "RuleCount": 1,
                "ItemCount": 91,
                "HostCount": 8,
                "IsDefault": 0
            },
            {
                "PolicyName": "CIS基线",
                "DetectInterval": 3,
                "DetectTime": "17:00:00",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22
                ],
                "HostIds": [],
                "HostIps": [
                    ""
                ],
                "PolicyId": 59,
                "RuleCount": 12,
                "ItemCount": 1427,
                "HostCount": 8,
                "IsDefault": 1
            },
            {
                "PolicyName": "ggg",
                "DetectInterval": 3,
                "DetectTime": "21:37:30",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    11
                ],
                "HostIds": [],
                "HostIps": [
                    ""
                ],
                "PolicyId": 171,
                "RuleCount": 1,
                "ItemCount": 91,
                "HostCount": 8,
                "IsDefault": 0
            },
            {
                "PolicyName": "自定义",
                "DetectInterval": 1,
                "DetectTime": "09:35:30",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    35184372088841
                ],
                "HostIds": [],
                "HostIps": [
                    ""
                ],
                "PolicyId": 161,
                "RuleCount": 1,
                "ItemCount": 1,
                "HostCount": 8,
                "IsDefault": 0
            },
            {
                "PolicyName": "test1",
                "DetectInterval": 1,
                "DetectTime": "02:00:00",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    11
                ],
                "HostIds": [],
                "HostIps": [
                    ""
                ],
                "PolicyId": 268,
                "RuleCount": 1,
                "ItemCount": 91,
                "HostCount": 8,
                "IsDefault": 0
            },
            {
                "PolicyName": "全部",
                "DetectInterval": 1,
                "DetectTime": "09:35:30",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    50,
                    51,
                    52,
                    53,
                    54,
                    55,
                    56,
                    57,
                    58,
                    70,
                    71,
                    72,
                    73,
                    74,
                    75,
                    76,
                    90,
                    91,
                    100,
                    101,
                    102,
                    103,
                    104,
                    105,
                    106,
                    120,
                    121,
                    122,
                    123,
                    124,
                    125,
                    126,
                    127,
                    128,
                    129,
                    130,
                    131,
                    132,
                    133,
                    134,
                    135,
                    136,
                    35184372088833,
                    35184372088835,
                    35184372088836,
                    35184372088841,
                    35184372088842,
                    35184372088843,
                    35184372088844,
                    35184372088846,
                    35184372088847,
                    35184372088848
                ],
                "HostIds": [],
                "HostIps": [
                    ""
                ],
                "PolicyId": 168,
                "RuleCount": 76,
                "ItemCount": 2955,
                "HostCount": 8,
                "IsDefault": 0
            },
            {
                "PolicyName": "等保三级",
                "DetectInterval": 1,
                "DetectTime": "17:00:00",
                "IsEnabled": 1,
                "AssetType": 0,
                "RuleIds": [
                    30,
                    31,
                    32,
                    33,
                    34
                ],
                "HostIds": [],
                "HostIps": [],
                "PolicyId": 61,
                "RuleCount": 5,
                "ItemCount": 173,
                "HostCount": 8,
                "IsDefault": 1
            },
            {
                "PolicyName": "专业版主机弱口令+旗舰版",
                "DetectInterval": 1,
                "DetectTime": "00:00:00",
                "IsEnabled": 1,
                "AssetType": 1,
                "RuleIds": [
                    50
                ],
                "HostIds": [
                    "044889f8-d6a2-4fc3-a8a8-c114b6f5266b",
                    "a0770b41-9697-4a1d-8150-b8fa247b6189",
                    "cc0e8a25-7169-4b5c-a929-2b4cccbfce10"
                ],
                "HostIps": [
                    ""
                ],
                "PolicyId": 172,
                "RuleCount": 1,
                "ItemCount": 1,
                "HostCount": 3,
                "IsDefault": 0
            }
        ],
        "RequestId": "5c340825-dbc9-4410-a47f-75eab15769d7",
        "Total": 19
    }
}
```

