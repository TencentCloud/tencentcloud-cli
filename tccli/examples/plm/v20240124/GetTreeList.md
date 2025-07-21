**Example 1: 示例**



Input: 

```
tccli plm GetTreeList --cli-unfold-argument  \
    --Type 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Code": "HA00010",
                "Name": "HA00010",
                "Level": 1,
                "Status": 1,
                "Weight": 1,
                "CenterIds": [
                    1
                ],
                "DepartmentIds": [
                    1
                ],
                "Child": [
                    {
                        "Code": "HB00010",
                        "Name": "HB00010",
                        "Level": 1,
                        "Status": 1,
                        "Weight": 1,
                        "CenterIds": [
                            1
                        ],
                        "DepartmentIds": [
                            1
                        ],
                        "Child": [
                            {
                                "Code": "CC00010",
                                "Name": "CC00010",
                                "Level": 1,
                                "Status": 1,
                                "Weight": 1,
                                "CenterIds": [
                                    1
                                ],
                                "DepartmentIds": [
                                    1
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "sdsjdfw12abc"
    }
}
```

