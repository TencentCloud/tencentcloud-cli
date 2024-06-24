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
                "ProjectID": "abc",
                "TemplateID": "abc",
                "Name": "abc",
                "DisplayName": "abc",
                "ProjectDisplayName": "abc",
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
                                    ],
                                    "Effective": "abc",
                                    "Workflow": {
                                        "Name": "abc",
                                        "ComponentName": "abc",
                                        "Count": 1,
                                        "Interval": 1
                                    },
                                    "FeatureAffinity": {
                                        "FeatureTerms": [
                                            {
                                                "FeaturesID": [
                                                    "abc"
                                                ],
                                                "Operator": "abc"
                                            }
                                        ]
                                    }
                                }
                            }
                        }
                    ]
                },
                "Creator": {
                    "Tencent": {
                        "Name": "abc"
                    }
                },
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "UpdatedAt": "2020-09-22T00:00:00+00:00"
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

