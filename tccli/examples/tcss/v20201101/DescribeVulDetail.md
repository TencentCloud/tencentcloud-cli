**Example 1: 查询漏洞详情**



Input: 

```
tccli tcss DescribeVulDetail --cli-unfold-argument  \
    --PocID 1
```

Output: 
```
{
    "Response": {
        "VulInfo": {
            "Category": "xx",
            "CVEID": "xx",
            "RegistryImageCount": 0,
            "LocalNewestImageCount": 0,
            "PocID": "xx",
            "CategoryType": "xx",
            "RegistryNewestImageCount": 0,
            "Description": "xx",
            "Tags": [
                "xx"
            ],
            "DefendedCount": 0,
            "DefenceHostCount": 0,
            "DefenceScope": "xx",
            "Name": "xx",
            "Level": "xx",
            "CVSSV3Score": 0.0,
            "OfficialSolution": "xx",
            "LocalImageCount": 0,
            "ComponentList": [
                {
                    "Version": [
                        "xx"
                    ],
                    "Name": "xx",
                    "FixedVersion": [
                        "xx"
                    ]
                }
            ],
            "ScanStatus": "xx",
            "CVSSV3Desc": "xx",
            "DefenseSolution": "xx",
            "DefenceStatus": "xx",
            "SubmitTime": "xx",
            "ContainerCount": 0,
            "Reference": [
                "xx"
            ]
        },
        "RequestId": "xx"
    }
}
```

