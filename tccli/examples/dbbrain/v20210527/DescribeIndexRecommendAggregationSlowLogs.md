**Example 1: 查询实例慢查询聚合结果**



Input: 

```
tccli dbbrain DescribeIndexRecommendAggregationSlowLogs --cli-unfold-argument  \
    --Product abc \
    --InstanceId abc \
    --Db abc \
    --Collection abc \
    --Signs abc
```

Output: 
```
{
    "Response": {
        "RequestId": "asdfaskldfanhasdfsd",
        "Aggregation": {
            "AvgExecTime": 8205,
            "AvgDocsExamined": 2765962,
            "SlowLogCount": 0,
            "SlowLogs": [
                "{\"t\":{\"$date\":\"2023-09-18T10:57:32.072+08:00\"},\"s\":\"I\",  \"c\":\"COMMAND\",  \"id\":51803,   \"ctx\":\"conn7221917\",\"msg\":\"Slow query\",\"attr\":{\"type\":\"command\",\"ns\":\"welabel.ground_truth_data\",\"appName\":\"MongoDB Compass\",\"command\":{\"aggregate\":\"ground_truth_data\",\"pipeline\":[{\"$match\":{\"is_skip\":{\"$ne\":true}}},{\"$project\":{\"labels\":{\"$filter\":{\"input\":\"$comments.data.error_labels\",\"as\":\"com\",\"cond\":{\"$eq\":[\"$$com.questionType\",\"single\"]}}},\"ground_truth_id\":1}},{\"$unwind\":{\"path\":\"$labels\"}},{\"$match\":{\"labels.relationshipType\":\"multi_image_group\"}},{\"$limit\":100000},{\"$group\":{\"_id\":{\"uid\":\"$labels.questionId\",\"element_id\":\"$labels.elementId\",\"gt_id\":\"$ground_truth_id\"}}},{\"$limit\":10}],\"allowDiskUse\":true,\"cursor\":{},\"maxTimeMS\":60000,\"lsid\":{\"id\":{\"$uuid\":\"dcda39f2-cb81-47be-ba04-b0078cf6cc7f\"}},\"$clusterTime\":{\"clusterTime\":{\"$timestamp\":{\"t\":1695005847,\"i\":9}},\"signature\":{\"hash\":{\"$binary\":{\"base64\":\"04MsomRxChDbiOVh1kjTHEsL644=\",\"subType\":\"0\"}},\"keyId\":7218831488945487874}},\"$db\":\"welabel\"},\"planSummary\":\"COLLSCAN\",\"numYields\":1067,\"queryHash\":\"A480F99A\",\"planCacheKey\":\"E2805889\",\"ok\":0,\"errMsg\":\"Error in $cursor stage :: caused by :: operation was interrupted\",\"errName\":\"Interrupted\",\"errCode\":11601,\"reslen\":276,\"locks\":{\"ReplicationStateTransition\":{\"acquireCount\":{\"w\":1144}},\"Global\":{\"acquireCount\":{\"r\":1144}},\"Database\":{\"acquireCount\":{\"r\":1144}},\"Collection\":{\"acquireCount\":{\"r\":1144}},\"Mutex\":{\"acquireCount\":{\"r\":77}}},\"protocol\":\"op_msg\",\"durationMillis\":3663}}",
                "{\"t\":{\"$date\":\"2023-09-18T10:57:27.730+08:00\"},\"s\":\"I\",  \"c\":\"COMMAND\",  \"id\":51803,   \"ctx\":\"conn7221917\",\"msg\":\"Slow query\",\"attr\":{\"type\":\"command\",\"ns\":\"welabel.ground_truth_data\",\"appName\":\"MongoDB Compass\",\"command\":{\"aggregate\":\"ground_truth_data\",\"pipeline\":[{\"$match\":{\"is_skip\":{\"$ne\":true}}},{\"$unwind\":{\"path\":\"$comments\"}},{\"$project\":{\"labels\":{\"$filter\":{\"input\":\"$comments.data.error_labels\",\"as\":\"com\",\"cond\":{\"$eq\":[\"$$com.questionType\",\"single\"]}}},\"ground_truth_id\":1}},{\"$unwind\":{\"path\":\"$labels\"}},{\"$match\":{\"labels.relationshipType\":\"multi_image_group\"}},{\"$limit\":100000},{\"$group\":{\"_id\":{\"uid\":\"$labels.questionId\",\"element_id\":\"$labels.elementId\",\"gt_id\":\"$ground_truth_id\"}}},{\"$limit\":10}],\"allowDiskUse\":true,\"cursor\":{},\"maxTimeMS\":60000,\"lsid\":{\"id\":{\"$uuid\":\"8532ddbf-2f1c-4bdd-a4f0-af0217f42607\"}},\"$clusterTime\":{\"clusterTime\":{\"$timestamp\":{\"t\":1695005524,\"i\":8}},\"signature\":{\"hash\":{\"$binary\":{\"base64\":\"60J0bCCsS5xTPDOE2yE4yWuxNr0=\",\"subType\":\"0\"}},\"keyId\":7218831488945487874}},\"$db\":\"welabel\"},\"planSummary\":\"COLLSCAN\",\"numYields\":2887,\"queryHash\":\"A1933E73\",\"planCacheKey\":\"77FB924F\",\"ok\":0,\"errMsg\":\"operation was interrupted\",\"errName\":\"Interrupted\",\"errCode\":11601,\"reslen\":237,\"locks\":{\"ReplicationStateTransition\":{\"acquireCount\":{\"w\":3004}},\"Global\":{\"acquireCount\":{\"r\":3004}},\"Database\":{\"acquireCount\":{\"r\":3004}},\"Collection\":{\"acquireCount\":{\"r\":3004}},\"Mutex\":{\"acquireCount\":{\"r\":117}}},\"protocol\":\"op_msg\",\"durationMillis\":10483}}"
            ],
            "SortCount": 0
        }
    }
}
```

