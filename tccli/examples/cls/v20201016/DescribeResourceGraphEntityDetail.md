**Example 1: success**



Input: 

```
tccli cls DescribeResourceGraphEntityDetail --cli-unfold-argument  \
    --EntityId 322c008927ab772835d9cc34be4d5287 \
    --ResourceGraphId 377f703a-6fab-41a9-b05a-636f06283a3f
```

Output: 
```
{
    "Response": {
        "EntityInfo": {
            "Attributes": [
                {
                    "Key": "instance_id",
                    "Value": "cdb-aav0v207"
                }
            ],
            "Domain": "tc",
            "EntityClassName": "tc.cdb.instance",
            "EntityId": "322c008927ab772835d9cc34be4d5287",
            "EntityName": "resource_test",
            "Product": "cdb",
            "RelatedLogTopics": [
                {
                    "BizType": 0,
                    "LogType": "slowlog",
                    "Region": "ap-guangzhou",
                    "TopicId": "a35a8ea8-253e-47bb-9d16-41a514827d86"
                }
            ],
            "ResourceId": "cdb-aav0v207",
            "Tags": []
        },
        "RequestId": "eb3d359b-2928-49b9-ad42-2a860138203b"
    }
}
```

