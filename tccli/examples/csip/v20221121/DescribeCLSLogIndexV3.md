**Example 1: DescribeCLSLogIndexV3-test1**



Input: 

```
tccli csip DescribeCLSLogIndexV3 --cli-unfold-argument  \
    --Filters.0.Key topicId \
    --Filters.0.Values csip-test-logaccess-251308491-tcss-process_port_assets \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TopicIndexInfos": [
            {
                "IncludeInternalFields": false,
                "MetadataFlag": 0,
                "ModifyTime": "2026-04-20 17:29:52",
                "Rule": {
                    "DynamicIndex": {
                        "Status": true
                    },
                    "FullText": {
                        "CaseSensitive": false,
                        "ContainZH": true,
                        "Tokenizer": "@&()='\",;:<>[]{}/ \n\t\r\\"
                    },
                    "KeyValue": {
                        "CaseSensitive": false,
                        "KeyValues": [
                            {
                                "Key": "container_id",
                                "Value": {
                                    "Alias": "",
                                    "ContainZH": true,
                                    "SqlFlag": true,
                                    "Tokenizer": "@&?|#()='\",;:<>[]{}/ \n\t\r\\",
                                    "Type": "text"
                                }
                            }
                        ]
                    }
                },
                "Status": true,
                "TopicId": "csip-test-logaccess-251308491-tcss-process_port_assets"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d5582c09-3297-4d31-902c-abc50f5a90be"
    }
}
```

**Example 2: DescribeCLSLogIndexV3-test2**



Input: 

```
tccli csip DescribeCLSLogIndexV3 --cli-unfold-argument  \
    --Filters.0.Key topicId \
    --Filters.0.Values 93-8056-4113-8f3e-82a4e16e \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TopicIndexInfos": [
            {
                "IncludeInternalFields": true,
                "MetadataFlag": 1,
                "ModifyTime": "2026-05-14 10:00:00",
                "Rule": {
                    "DynamicIndex": {
                        "Status": true
                    },
                    "FullText": {
                        "CaseSensitive": false,
                        "ContainZH": true,
                        "Tokenizer": "@&()='\",;:<>[]{}/ \n\t\r"
                    },
                    "KeyValue": {
                        "CaseSensitive": false,
                        "KeyValues": [
                            {
                                "Key": "level",
                                "Value": {
                                    "Alias": "log_level",
                                    "ContainZH": false,
                                    "SqlFlag": true,
                                    "Tokenizer": "@&()='\",;:<>[]{}/ \n\t\r",
                                    "Type": "text"
                                }
                            }
                        ]
                    },
                    "Tag": {
                        "CaseSensitive": false,
                        "KeyValues": [
                            {
                                "Key": "__FILENAME__",
                                "Value": {
                                    "Alias": "filename",
                                    "ContainZH": false,
                                    "SqlFlag": true,
                                    "Tokenizer": "@&()='\",;:<>[]{}/ \n\t\r",
                                    "Type": "text"
                                }
                            }
                        ]
                    }
                },
                "Status": true,
                "TopicId": "mock-topic-id-251308491"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e744f19b-71f4-4583-80e2-8dec444150f2"
    }
}
```

