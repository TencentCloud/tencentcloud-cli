**Example 1: 查询源集群消费组列表**

查询源集群消费组列表

Input: 

```
tccli tdmq DescribeRocketMQSourceClusterGroupList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --TaskId 700000780519-o4n3m5g97wgr-3391d15d
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Groups": [
            {
                "GroupName": "CID_ONSAPI_OWNER",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_10977",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "CID_ONSAPI_PULL",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_11578",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_10524",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_10178",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_10506",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_10370",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_1039",
                "Imported": false,
                "Namespace": "tdmq_default",
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_1049",
                "Imported": true,
                "Namespace": "tdmq_default",
                "Remark": ""
            }
        ],
        "RequestId": "5c27cf42-a31c-4605-9cfd-115a8414fef9",
        "TotalCount": 308
    }
}
```

**Example 2: 标准请求**

标准请求

Input: 

```
tccli tdmq DescribeRocketMQSourceClusterGroupList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --TaskId 700000780521-migratetest-d93e34d2
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Groups": [
            {
                "GroupName": "ConsumerGroup_3503",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_998",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_25517",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_13781",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_6815",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_7522",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_29106",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_10204",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_27223",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            },
            {
                "GroupName": "ConsumerGroup_8601",
                "Imported": false,
                "Namespace": null,
                "Remark": null
            }
        ],
        "RequestId": "a99c8984-c523-44e0-a019-2362015e8253",
        "TotalCount": 10
    }
}
```

