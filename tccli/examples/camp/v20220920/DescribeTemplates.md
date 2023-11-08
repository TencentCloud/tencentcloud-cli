**Example 1: DescribeTemplates**



Input: 

```
tccli camp DescribeTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateID": "abc",
                "Name": "abc",
                "DisplayName": "abc",
                "Description": "abc",
                "Content": "abc",
                "Type": "abc",
                "TemplateContent": {
                    "Component": "abc",
                    "Placements": [
                        {
                            "Name": "abc",
                            "Type": "abc",
                            "Properties": {
                                "Placement": {
                                    "Type": "abc",
                                    "Region": "abc",
                                    "Zones": [
                                        {
                                            "Zone": "abc",
                                            "Weight": 0
                                        }
                                    ],
                                    "MinZones": 0,
                                    "MaxZones": 0,
                                    "Components": [
                                        "abc"
                                    ],
                                    "Strategy": "abc",
                                    "Selector": [
                                        {
                                            "Key": "abc",
                                            "Value": "abc"
                                        }
                                    ],
                                    "Clusters": [
                                        "abc"
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        ],
        "Filters": [
            {
                "Name": "abc",
                "Values": [
                    "abc"
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

