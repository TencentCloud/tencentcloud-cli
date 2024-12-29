**Example 1: 获取诊断事件详情**



Input: 

```
tccli dbbrain DescribeDBDiagEvent --cli-unfold-argument  \
    --InstanceId cdb-test1234 \
    --EventId 5
```

Output: 
```
{
    "Response": {
        "Suggestions": "[{\"DataType\":\"title\",\"Data\":{\"Name\":\"SQL优化\"}},[{\"DataType\":\"sqlAdvice\",\"Data\":{\"Advices\":[{\"TableName\":\"t1\",\"TableSchema\":\"demo\",\"Keys\":[{\"SqlText\":\"alter table `demo`.`t1` add index index_0(`c_time`);\"}]}],\"Comments\":[],\"Schema\":\"demo\",\"SqlPlan\":{},\"SqlText\":\"select t1.*, t2.* from t1, t2 where t1.c_time = t2.c_time and t1.name > t2.name order by t2.name limit 10\",\"Tables\":[{\"TableName\":\"t1\",\"TableSchema\":\"demo\",\"TableDDL\":\"CREATE TABLE `t1` (\\n `id` int NOT NULL AUTO_INCREMENT,\\n `c_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,\\n `name` varchar(32) DEFAULT NULL,\\n `age` int NOT NULL DEFAULT '0',\\n PRIMARY KEY (`id`)\\n) ENGINE=InnoDB AUTO_INCREMENT=786393 DEFAULT CHARSET=utf8mb3\"}],\"Cost\":{\"Before\":1.060202269597E10,\"After\":1.060202269597E10,\"Ratio\":0}}}]]",
        "DiagType": "数据库快照",
        "EndTime": "2019-11-06 12:05:50",
        "RequestId": "78cf7bb1-0608-11ea-a9ef-2736f0f7f829",
        "Explanation": "[{\"DataType\":\"title\",\"Data\":{\"Name\":\"慢会话详情\"}},[{\"Layout\":\"vertical\",\"DataType\":\"table\",\"Data\":{\"Names\":[\"Schema\",{\"Type\":\"sql\",\"Name\":\"SqlText\"}],\"Data\":[{\"Schema\":\"demo\",\"SqlText\":\"select t1.*, t2.* from t1, t2 where t1.c_time = t2.c_time and t1.name > t2.name order by t2.name limit 10\"}]}}]]",
        "StartTime": "2019-11-06 12:05:40",
        "Severity": 4,
        "EventId": 5,
        "Outline": "数据库健康检查，发现1个问题",
        "Problem": "[{\"DataType\":\"title\",\"Data\":{\"Name\":\"会话快照\"}},{\"DataType\":\"title\",\"Data\":{\"Name\":\"事务快照\"}},{\"DataType\":\"title\",\"Data\":{\"Name\":\"Innodb状态快照\"}}]",
        "Metric": "",
        "DiagItem": "健康巡检"
    }
}
```

