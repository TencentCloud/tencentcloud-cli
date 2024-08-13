**Example 1: 创建表**

在demo库下创建一个test表

Input: 

```
tccli cdwdoris CreateTable --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --DbName demo \
    --TableName test \
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
    --Columns.3.DefaultValue 1970-01-01 00:00:00 \
    --Columns.3.IsKey False \
    --Columns.3.IsPartition False \
    --Columns.3.IsDistribution False \
    --Columns.3.Comment 用户最后一次访问时间 \
    --Columns.4.Name cost \
    --Columns.4.Type BIGINT \
    --Columns.4.AggType SUM \
    --Columns.4.IsNull False \
    --Columns.4.DefaultValue 0 \
    --Columns.4.IsKey False \
    --Columns.4.IsPartition False \
    --Columns.4.IsDistribution False \
    --Columns.4.Comment 用户总消费 \
    --Partition.AutoPartition False \
    --Partition.PartitionType Range \
    --Partition.RangeInfos.0.RangeType LESS THAN \
    --Partition.RangeInfos.0.PartitionName 0201 \
    --Partition.RangeInfos.0.Max ("2017-02-01") \
    --Partition.RangeInfos.1.RangeType FIXED \
    --Partition.RangeInfos.1.PartitionName 0202 \
    --Partition.RangeInfos.1.Left ("2011-02-01") \
    --Partition.RangeInfos.1.Right ("2012-02-01") \
    --Distribution.DistributionType Hash \
    --Distribution.Count 3 \
    --TableComment example \
    --Properties.0.PropertyKey replication_allocation \
    --Properties.0.PropertyValue tag.location.default: 1
```

Output: 
```
{
    "Response": {
        "RequestId": "f8f5e0af-7d36-4b49-8b4d-9c103deef55a"
    }
}
```

