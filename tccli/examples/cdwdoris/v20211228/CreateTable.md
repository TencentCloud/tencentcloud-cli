**Example 1: 建表-聚合模型**

建表-聚合模型

Input: 

```
tccli cdwdoris CreateTable --cli-unfold-argument  \
    --InstanceId cdwdoris-lrqz7cd4 \
    --DbName demo \
    --TableName t_name \
    --KeysType AGG_KEY \
    --Columns.0.Name user_id \
    --Columns.0.Type LARGEINT \
    --Columns.0.IsNull False \
    --Columns.0.IsKey True \
    --Columns.0.IsPartition False \
    --Columns.0.IsDistribution True \
    --Columns.0.Comment 用户id \
    --Columns.1.Name date \
    --Columns.1.Type DATE \
    --Columns.1.IsNull False \
    --Columns.1.IsKey True \
    --Columns.1.IsPartition True \
    --Columns.1.IsDistribution False \
    --Columns.1.Comment 数据灌入日期时间 \
    --Columns.2.Name city \
    --Columns.2.Type VARCHAR(20) \
    --Columns.2.IsNull True \
    --Columns.2.IsKey True \
    --Columns.2.IsPartition False \
    --Columns.2.IsDistribution False \
    --Columns.2.Comment 用户所在城市 \
    --Columns.3.Name last_visit_date \
    --Columns.3.Type DATETIME \
    --Columns.3.AggType REPLACE \
    --Columns.3.IsNull False \
    --Columns.3.IsKey False \
    --Columns.3.DefaultValue 1970-01-01 00:00:00 \
    --Columns.3.IsPartition False \
    --Columns.3.IsDistribution False \
    --Columns.3.Comment 用户最后一次访问时间 \
    --Columns.4.Name cost \
    --Columns.4.Type BIGINT \
    --Columns.4.AggType SUM \
    --Columns.4.IsNull False \
    --Columns.4.IsKey False \
    --Columns.4.DefaultValue 0 \
    --Columns.4.IsPartition False \
    --Columns.4.IsDistribution False \
    --Columns.4.Comment 用户总消费 \
    --Distribution.DistributionType Hash \
    --Distribution.Count 3 \
    --Partition.PartitionType Range \
    --Partition.AutoPartition False \
    --Partition.RangeInfos.0.RangeType LESS THAN \
    --Partition.RangeInfos.0.PartitionName p201701 \
    --Partition.RangeInfos.0.Max ("2017-02-01") \
    --Partition.RangeInfos.1.RangeType FIXED \
    --Partition.RangeInfos.1.PartitionName a202 \
    --Partition.RangeInfos.1.Left ("2017-02-02") \
    --Partition.RangeInfos.1.Right ("2017-03-01") \
    --TableComment example \
    --Properties.0.PropertyKey replication_allocation \
    --Properties.0.PropertyValue tag.location.default: 1
```

Output: 
```
{
    "Response": {
        "Message": "",
        "RequestId": "feef710c-431d-443b-b5fb-bc7ca25bfafd"
    }
}
```

**Example 2: 建表-明细模型**

建表-明细模型

Input: 

```
tccli cdwdoris CreateTable --cli-unfold-argument  \
    --InstanceId cdwdoris-lrqz7cd4 \
    --DbName demo \
    --TableName dup_test \
    --KeysType DUP_KEY \
    --Columns.0.Name timestamp \
    --Columns.0.Type DATETIME \
    --Columns.0.IsNull False \
    --Columns.0.IsKey True \
    --Columns.0.IsPartition False \
    --Columns.0.IsDistribution False \
    --Columns.0.Comment 日志时间 \
    --Columns.1.Name type \
    --Columns.1.Type INT \
    --Columns.1.IsNull False \
    --Columns.1.IsKey True \
    --Columns.1.IsPartition False \
    --Columns.1.IsDistribution True \
    --Columns.1.Comment 日志类型 \
    --Columns.2.Name error_code \
    --Columns.2.Type INT \
    --Columns.2.IsNull True \
    --Columns.2.IsKey True \
    --Columns.2.IsPartition False \
    --Columns.2.IsDistribution False \
    --Columns.2.Comment 错误码 \
    --Columns.3.Name error_msg \
    --Columns.3.Type VARCHAR(1024) \
    --Columns.3.IsNull True \
    --Columns.3.IsKey False \
    --Columns.3.IsPartition False \
    --Columns.3.IsDistribution False \
    --Columns.3.Comment 错误详细信息 \
    --Columns.4.Name op_id \
    --Columns.4.Type BIGINT \
    --Columns.4.IsNull True \
    --Columns.4.IsKey False \
    --Columns.4.IsPartition False \
    --Columns.4.IsDistribution False \
    --Columns.4.Comment 负责人id \
    --Columns.5.Name op_time \
    --Columns.5.Type DATETIME \
    --Columns.5.IsNull True \
    --Columns.5.Comment 处理时间 \
    --Distribution.DistributionType Hash \
    --Distribution.Count 1 \
    --Properties.0.PropertyKey replication_allocation \
    --Properties.0.PropertyValue tag.location.default: 1
```

Output: 
```
{
    "Response": {
        "Message": "",
        "RequestId": "1b12e7c9-4802-412c-b23b-5a2514f508a8"
    }
}
```

**Example 3: 建表-主键模型**

建表-主键模型

Input: 

```
tccli cdwdoris CreateTable --cli-unfold-argument  \
    --InstanceId cdwdoris-lrqz7cd4 \
    --DbName demo \
    --TableName uni_test1 \
    --KeysType UNI_KEY \
    --Columns.0.Name user_id \
    --Columns.0.Type LARGEINT \
    --Columns.0.IsNull False \
    --Columns.0.IsKey True \
    --Columns.0.IsPartition False \
    --Columns.0.IsDistribution True \
    --Columns.0.Comment 用户id \
    --Columns.1.Name username \
    --Columns.1.Type VARCHAR(50) \
    --Columns.1.IsNull False \
    --Columns.1.IsKey True \
    --Columns.1.IsPartition False \
    --Columns.1.IsDistribution False \
    --Columns.1.Comment 用户昵称 \
    --Columns.2.Name city \
    --Columns.2.Type VARCHAR(20) \
    --Columns.2.IsNull True \
    --Columns.2.IsKey False \
    --Columns.2.IsPartition False \
    --Columns.2.IsDistribution False \
    --Columns.2.Comment 用户所在城市 \
    --Columns.3.Name age \
    --Columns.3.Type SMALLINT \
    --Columns.3.IsNull True \
    --Columns.3.IsKey False \
    --Columns.3.IsPartition False \
    --Columns.3.IsDistribution False \
    --Columns.3.Comment 用户年龄 \
    --Columns.4.Name sex \
    --Columns.4.Type TINYINT \
    --Columns.4.IsNull True \
    --Columns.4.IsKey False \
    --Columns.4.IsPartition False \
    --Columns.4.IsDistribution False \
    --Columns.4.Comment 用户性别 \
    --Columns.5.Name phone \
    --Columns.5.Type LARGEINT \
    --Columns.5.IsNull True \
    --Columns.5.Comment 用户电话 \
    --Columns.6.Name address \
    --Columns.6.Type VARCHAR(500) \
    --Columns.6.IsNull True \
    --Columns.6.Comment 用户地址 \
    --Columns.7.Name register_time \
    --Columns.7.Type DATETIME \
    --Columns.7.IsNull True \
    --Columns.7.Comment 用户注册时间 \
    --Distribution.DistributionType Hash \
    --Distribution.Count 1 \
    --Properties.0.PropertyKey replication_allocation \
    --Properties.0.PropertyValue tag.location.default: 1
```

Output: 
```
{
    "Response": {
        "Message": "",
        "RequestId": "1e10c4a5-44cf-4833-be5b-cb5fb8217c43"
    }
}
```

