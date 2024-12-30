**Example 1: 示例1**



Input: 

```
tccli mna GetL3ConnList --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1 \
    --DeviceId mna-2x2tllhb18
```

Output: 
```
{
    "Response": {
        "L3ConnList": [
            {
                "L3ConnId": "l3conn-h9boibynmp",
                "DeviceId1": "mna-2x2tllhb18",
                "Cidr1": "192.168.1.0/26",
                "DeviceId2": "mna-2x2tllhb13",
                "Cidr2": "192.168.1.0/26",
                "Enable": true,
                "Description": "test"
            }
        ],
        "Length": 1,
        "TotalPage": 1,
        "RequestId": "e5b299c7-aaf4-4a5e-9d01-feb63273e347"
    }
}
```

