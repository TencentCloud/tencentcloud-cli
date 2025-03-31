**Example 1: 创建云产品投递任务**



Input: 

```
tccli cls CreateCloudProductLogCollection --cli-unfold-argument  \
    --InstanceId cdb-9edkkbdc \
    --AssumerName CDB \
    --LogType CDB-AUDIT \
    --CloudProductRegion qy \
    --ClsRegion ap-qingyuan \
    --LogsetName test-logset \
    --TopicName test-topic
```

Output: 
```
{
    "Response": {
        "LogsetId": "c227837e-29e6-4597-a22d-15265d8179c6",
        "LogsetName": "test-logset",
        "RequestId": "1acc4a4a-8231-4439-8a30-d082a95b9b43",
        "Status": 1,
        "TopicId": "9e041c76-869b-4eec-a54e-7f22f53e1afc",
        "TopicName": "test-topic"
    }
}
```

