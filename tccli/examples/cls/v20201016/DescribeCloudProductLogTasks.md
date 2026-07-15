**Example 1: DescribeCloudProductLogTasks**



Input: 

```
tccli cls DescribeCloudProductLogTasks --cli-unfold-argument  \
    --Filters.0.Key instanceId \
    --Filters.0.Values cfs-48afd4bff \
    --WithTags True
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "ClsRegion": "ap-guangzhou-open",
                "Extend": "rename",
                "InstanceId": "cfs-48afd4bff",
                "LogType": "han*****test",
                "LogsetId": "29ccb4c0-ab2f-47ab-9dcd-31413b057812",
                "LogsetTags": [
                    {
                        "Key": "name",
                        "Value": "业务B"
                    }
                ],
                "Status": 1,
                "TopicId": "c344124a-68c8-4d34-ac46-04676625065e",
                "TopicTags": [
                    {
                        "Key": "name",
                        "Value": "业务B"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "5218cfeb-1810-477c-8ead-f3eadc6f71f9"
    }
}
```

