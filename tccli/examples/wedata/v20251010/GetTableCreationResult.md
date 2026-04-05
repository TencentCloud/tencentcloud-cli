**Example 1: 文件到表任务结果查询接口**



Input: 

```
tccli wedata GetTableCreationResult --cli-unfold-argument  \
    --TaskId 20251017199916000001
```

Output: 
```
{
    "Response": {
        "RequestId": "5fbbe5a3-e2e0-4de6-9022-517120b25230",
        "Data": {
            "Data": [
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": "{\"city\":\"San Francisco\",\"state\":\"MA\",\"street\":\"507 Pine St\",\"zipcode\":\"26262\"}"
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": "976280"
                        },
                        {
                            "Name": "name",
                            "Value": "Olivia Chen"
                        },
                        {
                            "Name": "timestamp",
                            "Value": "2025-09-07 11:09:40"
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": null
                        },
                        {
                            "Name": "department",
                            "Value": "Engineering"
                        },
                        {
                            "Name": "id",
                            "Value": "390321"
                        },
                        {
                            "Name": "name",
                            "Value": "Olivia Chen"
                        },
                        {
                            "Name": "timestamp",
                            "Value": "2025-07-16 11:09:40"
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": "{\"city\":\"San Francisco\",\"state\":\"IL\",\"street\":\"486 Pine St\",\"zipcode\":\"87515\"}"
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": "814197"
                        },
                        {
                            "Name": "name",
                            "Value": "Nathan Wong"
                        },
                        {
                            "Name": "timestamp",
                            "Value": "2025-07-11 11:09:40"
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": "{\"city\":\"Boston\",\"state\":\"MA\",\"street\":\"402 Pine St\",\"zipcode\":\"54945\"}"
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": "928487"
                        },
                        {
                            "Name": "name",
                            "Value": "Olivia Chen"
                        },
                        {
                            "Name": "timestamp",
                            "Value": "2025-08-07 11:09:40"
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": "{\"city\":\"San Francisco\",\"state\":\"CA\",\"street\":\"475 Oak St\",\"zipcode\":\"69957\"}"
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": "317669"
                        },
                        {
                            "Name": "name",
                            "Value": "Nathan Wong"
                        },
                        {
                            "Name": "timestamp",
                            "Value": "2025-02-21 11:09:40"
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": null
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": null
                        },
                        {
                            "Name": "name",
                            "Value": null
                        },
                        {
                            "Name": "timestamp",
                            "Value": null
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": null
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": null
                        },
                        {
                            "Name": "name",
                            "Value": null
                        },
                        {
                            "Name": "timestamp",
                            "Value": null
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": null
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": null
                        },
                        {
                            "Name": "name",
                            "Value": null
                        },
                        {
                            "Name": "timestamp",
                            "Value": null
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": null
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": null
                        },
                        {
                            "Name": "name",
                            "Value": null
                        },
                        {
                            "Name": "timestamp",
                            "Value": null
                        }
                    ]
                },
                {
                    "Fields": [
                        {
                            "Name": "address",
                            "Value": null
                        },
                        {
                            "Name": "department",
                            "Value": null
                        },
                        {
                            "Name": "id",
                            "Value": null
                        },
                        {
                            "Name": "name",
                            "Value": null
                        },
                        {
                            "Name": "timestamp",
                            "Value": null
                        }
                    ]
                }
            ],
            "Schema": [
                {
                    "Name": "address",
                    "Type": "struct<city:string,state:string,street:string,zipcode:string>",
                    "Selected": false
                },
                {
                    "Name": "department",
                    "Type": "string",
                    "Selected": true
                },
                {
                    "Name": "id",
                    "Type": "bigint",
                    "Selected": false
                },
                {
                    "Name": "name",
                    "Type": "string",
                    "Selected": true
                },
                {
                    "Name": "timestamp",
                    "Type": "string",
                    "Selected": true
                }
            ]
        }
    }
}
```

