**Example 1: 创建SINK任务**

SINK任务

Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType SINK \
    --SourceResource.Type KAFKA \
    --SourceResource.KafkaParam.SelfBuilt False \
    --SourceResource.KafkaParam.Resource ckafka-7kd5rzza \
    --SourceResource.KafkaParam.Topic topic-test \
    --SourceResource.KafkaParam.OffsetType timestamp \
    --SourceResource.KafkaParam.StartTime 1635339533 \
    --TargetResource.Type EB \
    --TargetResource.EventBusParam.Type COS \
    --TargetResource.EventBusParam.SelfBuilt False \
    --TargetResource.EventBusParam.Resource target-resource \
    --TargetResource.EventBusParam.Namespace default \
    --TargetResource.EventBusParam.FunctionName ckafka-7kd5rzza_topic-0cus2p9z_task_1633501781881_schedule \
    --TargetResource.EventBusParam.Qualifier $LATEST
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "abc",
            "DatahubId": "abc"
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 创建SINK任务(ES)**



Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType SINK \
    --SourceResource.Type KAFKA \
    --SourceResource.KafkaParam.SelfBuilt False \
    --SourceResource.KafkaParam.Resource ckafka-7kd5rzza \
    --SourceResource.KafkaParam.Topic topic-test \
    --SourceResource.KafkaParam.OffsetType earliest \
    --TargetResource.Type ES \
    --TargetResource.EsParam.Resource resource-xxx \
    --TargetResource.EsParam.DropInvalidMessage True \
    --TargetResource.EsParam.Index xxx \
    --TargetResource.EsParam.DropInvalidJsonMessage False
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "abc",
            "DatahubId": "abc"
        },
        "RequestId": "abc"
    }
}
```

**Example 3: 创建TRANSFORM任务**

TRANSFORM任务

Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName abc \
    --TaskType abc \
    --SourceResource.Type abc \
    --SourceResource.KafkaParam.SelfBuilt True \
    --SourceResource.KafkaParam.Resource abc \
    --SourceResource.KafkaParam.Topic abc \
    --SourceResource.KafkaParam.OffsetType abc \
    --SourceResource.KafkaParam.StartTime 1 \
    --SourceResource.KafkaParam.ResourceName abc \
    --SourceResource.KafkaParam.ZoneId 0 \
    --SourceResource.KafkaParam.TopicId abc \
    --SourceResource.KafkaParam.PartitionNum 0 \
    --SourceResource.KafkaParam.EnableToleration True \
    --SourceResource.KafkaParam.QpsLimit 1 \
    --SourceResource.KafkaParam.TableMappings.0.Database abc \
    --SourceResource.KafkaParam.TableMappings.0.Table abc \
    --SourceResource.KafkaParam.TableMappings.0.Topic abc \
    --SourceResource.KafkaParam.TableMappings.0.TopicId abc \
    --SourceResource.KafkaParam.UseTableMapping True \
    --SourceResource.KafkaParam.UseAutoCreateTopic True \
    --SourceResource.KafkaParam.CompressionType abc \
    --SourceResource.KafkaParam.MsgMultiple 0 \
    --SourceResource.KafkaParam.ConnectorSyncType abc \
    --SourceResource.KafkaParam.KeepPartition True \
    --SourceResource.EventBusParam.Type abc \
    --SourceResource.EventBusParam.SelfBuilt True \
    --SourceResource.EventBusParam.Resource abc \
    --SourceResource.EventBusParam.Namespace abc \
    --SourceResource.EventBusParam.FunctionName abc \
    --SourceResource.EventBusParam.Qualifier abc \
    --SourceResource.MongoDBParam.Database abc \
    --SourceResource.MongoDBParam.Collection abc \
    --SourceResource.MongoDBParam.CopyExisting True \
    --SourceResource.MongoDBParam.Resource abc \
    --SourceResource.MongoDBParam.Ip abc \
    --SourceResource.MongoDBParam.Port 0 \
    --SourceResource.MongoDBParam.UserName abc \
    --SourceResource.MongoDBParam.Password abc \
    --SourceResource.MongoDBParam.ListeningEvent abc \
    --SourceResource.MongoDBParam.ReadPreference abc \
    --SourceResource.MongoDBParam.Pipeline abc \
    --SourceResource.MongoDBParam.SelfBuilt True \
    --SourceResource.EsParam.Resource abc \
    --SourceResource.EsParam.Port 0 \
    --SourceResource.EsParam.UserName abc \
    --SourceResource.EsParam.Password abc \
    --SourceResource.EsParam.SelfBuilt True \
    --SourceResource.EsParam.ServiceVip abc \
    --SourceResource.EsParam.UniqVpcId abc \
    --SourceResource.EsParam.DropInvalidMessage True \
    --SourceResource.EsParam.Index abc \
    --SourceResource.EsParam.DateFormat abc \
    --SourceResource.EsParam.ContentKey abc \
    --SourceResource.EsParam.DropInvalidJsonMessage True \
    --SourceResource.EsParam.DocumentIdField abc \
    --SourceResource.EsParam.IndexType abc \
    --SourceResource.EsParam.DropCls.DropInvalidMessageToCls True \
    --SourceResource.EsParam.DropCls.DropClsRegion abc \
    --SourceResource.EsParam.DropCls.DropClsOwneruin abc \
    --SourceResource.EsParam.DropCls.DropClsTopicId abc \
    --SourceResource.EsParam.DropCls.DropClsLogSet abc \
    --SourceResource.EsParam.DatabasePrimaryKey abc \
    --SourceResource.EsParam.DropDlq.Type abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.SelfBuilt True \
    --SourceResource.EsParam.DropDlq.KafkaParam.Resource abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.Topic abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.OffsetType abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.StartTime 1 \
    --SourceResource.EsParam.DropDlq.KafkaParam.ResourceName abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.ZoneId 0 \
    --SourceResource.EsParam.DropDlq.KafkaParam.TopicId abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.PartitionNum 0 \
    --SourceResource.EsParam.DropDlq.KafkaParam.EnableToleration True \
    --SourceResource.EsParam.DropDlq.KafkaParam.QpsLimit 1 \
    --SourceResource.EsParam.DropDlq.KafkaParam.TableMappings.0.Database abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.TableMappings.0.Table abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.TableMappings.0.Topic abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.TableMappings.0.TopicId abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.UseTableMapping True \
    --SourceResource.EsParam.DropDlq.KafkaParam.UseAutoCreateTopic True \
    --SourceResource.EsParam.DropDlq.KafkaParam.CompressionType abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.MsgMultiple 0 \
    --SourceResource.EsParam.DropDlq.KafkaParam.ConnectorSyncType abc \
    --SourceResource.EsParam.DropDlq.KafkaParam.KeepPartition True \
    --SourceResource.EsParam.DropDlq.RetryInterval 1 \
    --SourceResource.EsParam.DropDlq.MaxRetryAttempts 1 \
    --SourceResource.EsParam.DropDlq.TopicParam.Resource abc \
    --SourceResource.EsParam.DropDlq.TopicParam.OffsetType abc \
    --SourceResource.EsParam.DropDlq.TopicParam.StartTime 1 \
    --SourceResource.EsParam.DropDlq.TopicParam.TopicId abc \
    --SourceResource.EsParam.DropDlq.TopicParam.CompressionType abc \
    --SourceResource.EsParam.DropDlq.TopicParam.UseAutoCreateTopic True \
    --SourceResource.EsParam.DropDlq.TopicParam.MsgMultiple 0 \
    --SourceResource.EsParam.DropDlq.DlqType abc \
    --SourceResource.EsParam.RecordMappingList.0.ColumnName abc \
    --SourceResource.EsParam.RecordMappingList.0.JsonKey abc \
    --SourceResource.EsParam.DateField abc \
    --SourceResource.EsParam.RecordMappingMode abc \
    --SourceResource.TdwParam.Bid abc \
    --SourceResource.TdwParam.Tid abc \
    --SourceResource.TdwParam.IsDomestic True \
    --SourceResource.TdwParam.TdwHost abc \
    --SourceResource.TdwParam.TdwPort 0 \
    --SourceResource.DtsParam.Resource abc \
    --SourceResource.DtsParam.Ip abc \
    --SourceResource.DtsParam.Port 0 \
    --SourceResource.DtsParam.Topic abc \
    --SourceResource.DtsParam.GroupId abc \
    --SourceResource.DtsParam.GroupUser abc \
    --SourceResource.DtsParam.GroupPassword abc \
    --SourceResource.DtsParam.TranSql True \
    --SourceResource.ClickHouseParam.Ip abc \
    --SourceResource.ClickHouseParam.Port 0 \
    --SourceResource.ClickHouseParam.UserName abc \
    --SourceResource.ClickHouseParam.Password abc \
    --SourceResource.ClickHouseParam.Cluster abc \
    --SourceResource.ClickHouseParam.Database abc \
    --SourceResource.ClickHouseParam.Table abc \
    --SourceResource.ClickHouseParam.Schema.0.ColumnName abc \
    --SourceResource.ClickHouseParam.Schema.0.JsonKey abc \
    --SourceResource.ClickHouseParam.Schema.0.Type abc \
    --SourceResource.ClickHouseParam.Schema.0.AllowNull True \
    --SourceResource.ClickHouseParam.ServiceVip abc \
    --SourceResource.ClickHouseParam.UniqVpcId abc \
    --SourceResource.ClickHouseParam.Resource abc \
    --SourceResource.ClickHouseParam.SelfBuilt True \
    --SourceResource.ClickHouseParam.DropInvalidMessage True \
    --SourceResource.ClickHouseParam.Type abc \
    --SourceResource.ClickHouseParam.DropCls.DropInvalidMessageToCls True \
    --SourceResource.ClickHouseParam.DropCls.DropClsRegion abc \
    --SourceResource.ClickHouseParam.DropCls.DropClsOwneruin abc \
    --SourceResource.ClickHouseParam.DropCls.DropClsTopicId abc \
    --SourceResource.ClickHouseParam.DropCls.DropClsLogSet abc \
    --SourceResource.ClickHouseParam.BatchSize 0 \
    --SourceResource.ClickHouseParam.ConsumerFetchMinBytes 0 \
    --SourceResource.ClickHouseParam.ConsumerFetchMaxWaitMs 0 \
    --SourceResource.ClsParam.DecodeJson True \
    --SourceResource.ClsParam.Resource abc \
    --SourceResource.ClsParam.LogSet abc \
    --SourceResource.ClsParam.ContentKey abc \
    --SourceResource.ClsParam.TimeField abc \
    --SourceResource.CosParam.BucketName abc \
    --SourceResource.CosParam.Region abc \
    --SourceResource.CosParam.ObjectKey abc \
    --SourceResource.CosParam.AggregateBatchSize 1 \
    --SourceResource.CosParam.AggregateInterval 1 \
    --SourceResource.CosParam.FormatOutputType abc \
    --SourceResource.CosParam.ObjectKeyPrefix abc \
    --SourceResource.CosParam.DirectoryTimeFormat abc \
    --SourceResource.MySQLParam.Database abc \
    --SourceResource.MySQLParam.Table abc \
    --SourceResource.MySQLParam.Resource abc \
    --SourceResource.MySQLParam.SnapshotMode abc \
    --SourceResource.MySQLParam.DdlTopic abc \
    --SourceResource.MySQLParam.DataSourceMonitorMode abc \
    --SourceResource.MySQLParam.DataSourceMonitorResource abc \
    --SourceResource.MySQLParam.DataSourceIncrementMode abc \
    --SourceResource.MySQLParam.DataSourceIncrementColumn abc \
    --SourceResource.MySQLParam.DataSourceStartFrom abc \
    --SourceResource.MySQLParam.DataTargetInsertMode abc \
    --SourceResource.MySQLParam.DataTargetPrimaryKeyField abc \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.JsonKey abc \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.Type abc \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.AllowNull True \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.ColumnName abc \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.ExtraInfo abc \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.ColumnSize abc \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.DecimalDigits abc \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.AutoIncrement True \
    --SourceResource.MySQLParam.DataTargetRecordMapping.0.DefaultValue abc \
    --SourceResource.MySQLParam.TopicRegex abc \
    --SourceResource.MySQLParam.TopicReplacement abc \
    --SourceResource.MySQLParam.KeyColumns abc \
    --SourceResource.MySQLParam.DropInvalidMessage True \
    --SourceResource.MySQLParam.DropCls.DropInvalidMessageToCls True \
    --SourceResource.MySQLParam.DropCls.DropClsRegion abc \
    --SourceResource.MySQLParam.DropCls.DropClsOwneruin abc \
    --SourceResource.MySQLParam.DropCls.DropClsTopicId abc \
    --SourceResource.MySQLParam.DropCls.DropClsLogSet abc \
    --SourceResource.MySQLParam.OutputFormat abc \
    --SourceResource.MySQLParam.IsTablePrefix True \
    --SourceResource.MySQLParam.IncludeContentChanges abc \
    --SourceResource.MySQLParam.IncludeQuery True \
    --SourceResource.MySQLParam.RecordWithSchema True \
    --SourceResource.MySQLParam.SignalDatabase abc \
    --SourceResource.MySQLParam.IsTableRegular True \
    --SourceResource.MySQLParam.SignalTable abc \
    --SourceResource.MySQLParam.DateTimeZone abc \
    --SourceResource.MySQLParam.SelfBuilt True \
    --SourceResource.PostgreSQLParam.Database abc \
    --SourceResource.PostgreSQLParam.Table abc \
    --SourceResource.PostgreSQLParam.Resource abc \
    --SourceResource.PostgreSQLParam.PluginName abc \
    --SourceResource.PostgreSQLParam.SnapshotMode abc \
    --SourceResource.PostgreSQLParam.DataFormat abc \
    --SourceResource.PostgreSQLParam.DataTargetInsertMode abc \
    --SourceResource.PostgreSQLParam.DataTargetPrimaryKeyField abc \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.JsonKey abc \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.Type abc \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.AllowNull True \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.ColumnName abc \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.ExtraInfo abc \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.ColumnSize abc \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.DecimalDigits abc \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.AutoIncrement True \
    --SourceResource.PostgreSQLParam.DataTargetRecordMapping.0.DefaultValue abc \
    --SourceResource.PostgreSQLParam.DropInvalidMessage True \
    --SourceResource.PostgreSQLParam.IsTableRegular True \
    --SourceResource.PostgreSQLParam.KeyColumns abc \
    --SourceResource.PostgreSQLParam.RecordWithSchema True \
    --SourceResource.TopicParam.Resource abc \
    --SourceResource.TopicParam.OffsetType abc \
    --SourceResource.TopicParam.StartTime 1 \
    --SourceResource.TopicParam.TopicId abc \
    --SourceResource.TopicParam.CompressionType abc \
    --SourceResource.TopicParam.UseAutoCreateTopic True \
    --SourceResource.TopicParam.MsgMultiple 0 \
    --SourceResource.MariaDBParam.Database abc \
    --SourceResource.MariaDBParam.Table abc \
    --SourceResource.MariaDBParam.Resource abc \
    --SourceResource.MariaDBParam.SnapshotMode abc \
    --SourceResource.MariaDBParam.KeyColumns abc \
    --SourceResource.MariaDBParam.IsTablePrefix True \
    --SourceResource.MariaDBParam.OutputFormat abc \
    --SourceResource.MariaDBParam.IncludeContentChanges abc \
    --SourceResource.MariaDBParam.IncludeQuery True \
    --SourceResource.MariaDBParam.RecordWithSchema True \
    --SourceResource.SQLServerParam.Database abc \
    --SourceResource.SQLServerParam.Table abc \
    --SourceResource.SQLServerParam.Resource abc \
    --SourceResource.SQLServerParam.SnapshotMode abc \
    --SourceResource.CtsdbParam.Resource abc \
    --SourceResource.CtsdbParam.CtsdbMetric abc \
    --SourceResource.ScfParam.FunctionName abc \
    --SourceResource.ScfParam.Namespace abc \
    --SourceResource.ScfParam.Qualifier abc \
    --SourceResource.ScfParam.BatchSize 0 \
    --SourceResource.ScfParam.MaxRetries 0 \
    --SourceResource.MqttParam.Topics abc \
    --SourceResource.MqttParam.CleanSession True \
    --SourceResource.MqttParam.Resource abc \
    --SourceResource.MqttParam.Ip abc \
    --SourceResource.MqttParam.Port 0 \
    --SourceResource.MqttParam.UserName abc \
    --SourceResource.MqttParam.Password abc \
    --SourceResource.MqttParam.Qos 0 \
    --SourceResource.MqttParam.MaxTasks 0 \
    --SourceResource.MqttParam.ServiceVip abc \
    --SourceResource.MqttParam.UniqVpcId abc \
    --SourceResource.MqttParam.SelfBuilt True \
    --TargetResource.Type abc \
    --TargetResource.KafkaParam.SelfBuilt True \
    --TargetResource.KafkaParam.Resource abc \
    --TargetResource.KafkaParam.Topic abc \
    --TargetResource.KafkaParam.OffsetType abc \
    --TargetResource.KafkaParam.StartTime 1 \
    --TargetResource.KafkaParam.ResourceName abc \
    --TargetResource.KafkaParam.ZoneId 0 \
    --TargetResource.KafkaParam.TopicId abc \
    --TargetResource.KafkaParam.PartitionNum 0 \
    --TargetResource.KafkaParam.EnableToleration True \
    --TargetResource.KafkaParam.QpsLimit 1 \
    --TargetResource.KafkaParam.TableMappings.0.Database abc \
    --TargetResource.KafkaParam.TableMappings.0.Table abc \
    --TargetResource.KafkaParam.TableMappings.0.Topic abc \
    --TargetResource.KafkaParam.TableMappings.0.TopicId abc \
    --TargetResource.KafkaParam.UseTableMapping True \
    --TargetResource.KafkaParam.UseAutoCreateTopic True \
    --TargetResource.KafkaParam.CompressionType abc \
    --TargetResource.KafkaParam.MsgMultiple 0 \
    --TargetResource.KafkaParam.ConnectorSyncType abc \
    --TargetResource.KafkaParam.KeepPartition True \
    --TargetResource.EventBusParam.Type abc \
    --TargetResource.EventBusParam.SelfBuilt True \
    --TargetResource.EventBusParam.Resource abc \
    --TargetResource.EventBusParam.Namespace abc \
    --TargetResource.EventBusParam.FunctionName abc \
    --TargetResource.EventBusParam.Qualifier abc \
    --TargetResource.MongoDBParam.Database abc \
    --TargetResource.MongoDBParam.Collection abc \
    --TargetResource.MongoDBParam.CopyExisting True \
    --TargetResource.MongoDBParam.Resource abc \
    --TargetResource.MongoDBParam.Ip abc \
    --TargetResource.MongoDBParam.Port 0 \
    --TargetResource.MongoDBParam.UserName abc \
    --TargetResource.MongoDBParam.Password abc \
    --TargetResource.MongoDBParam.ListeningEvent abc \
    --TargetResource.MongoDBParam.ReadPreference abc \
    --TargetResource.MongoDBParam.Pipeline abc \
    --TargetResource.MongoDBParam.SelfBuilt True \
    --TargetResource.EsParam.Resource abc \
    --TargetResource.EsParam.Port 0 \
    --TargetResource.EsParam.UserName abc \
    --TargetResource.EsParam.Password abc \
    --TargetResource.EsParam.SelfBuilt True \
    --TargetResource.EsParam.ServiceVip abc \
    --TargetResource.EsParam.UniqVpcId abc \
    --TargetResource.EsParam.DropInvalidMessage True \
    --TargetResource.EsParam.Index abc \
    --TargetResource.EsParam.DateFormat abc \
    --TargetResource.EsParam.ContentKey abc \
    --TargetResource.EsParam.DropInvalidJsonMessage True \
    --TargetResource.EsParam.DocumentIdField abc \
    --TargetResource.EsParam.IndexType abc \
    --TargetResource.EsParam.DatabasePrimaryKey abc \
    --TargetResource.EsParam.DropDlq.Type abc \
    --TargetResource.EsParam.DropDlq.RetryInterval 1 \
    --TargetResource.EsParam.DropDlq.MaxRetryAttempts 1 \
    --TargetResource.EsParam.DropDlq.TopicParam.Resource abc \
    --TargetResource.EsParam.DropDlq.TopicParam.OffsetType abc \
    --TargetResource.EsParam.DropDlq.TopicParam.StartTime 1 \
    --TargetResource.EsParam.DropDlq.TopicParam.TopicId abc \
    --TargetResource.EsParam.DropDlq.TopicParam.CompressionType abc \
    --TargetResource.EsParam.DropDlq.TopicParam.UseAutoCreateTopic True \
    --TargetResource.EsParam.DropDlq.TopicParam.MsgMultiple 0 \
    --TargetResource.EsParam.DropDlq.DlqType abc \
    --TargetResource.EsParam.RecordMappingList.0.ColumnName abc \
    --TargetResource.EsParam.RecordMappingList.0.JsonKey abc \
    --TargetResource.EsParam.DateField abc \
    --TargetResource.EsParam.RecordMappingMode abc \
    --TargetResource.TdwParam.Bid abc \
    --TargetResource.TdwParam.Tid abc \
    --TargetResource.TdwParam.IsDomestic True \
    --TargetResource.TdwParam.TdwHost abc \
    --TargetResource.TdwParam.TdwPort 0 \
    --TargetResource.DtsParam.Resource abc \
    --TargetResource.DtsParam.Ip abc \
    --TargetResource.DtsParam.Port 0 \
    --TargetResource.DtsParam.Topic abc \
    --TargetResource.DtsParam.GroupId abc \
    --TargetResource.DtsParam.GroupUser abc \
    --TargetResource.DtsParam.GroupPassword abc \
    --TargetResource.DtsParam.TranSql True \
    --TargetResource.ClickHouseParam.Ip abc \
    --TargetResource.ClickHouseParam.Port 0 \
    --TargetResource.ClickHouseParam.UserName abc \
    --TargetResource.ClickHouseParam.Password abc \
    --TargetResource.ClickHouseParam.Cluster abc \
    --TargetResource.ClickHouseParam.Database abc \
    --TargetResource.ClickHouseParam.Table abc \
    --TargetResource.ClickHouseParam.Schema.0.ColumnName abc \
    --TargetResource.ClickHouseParam.Schema.0.JsonKey abc \
    --TargetResource.ClickHouseParam.Schema.0.Type abc \
    --TargetResource.ClickHouseParam.Schema.0.AllowNull True \
    --TargetResource.ClickHouseParam.ServiceVip abc \
    --TargetResource.ClickHouseParam.UniqVpcId abc \
    --TargetResource.ClickHouseParam.Resource abc \
    --TargetResource.ClickHouseParam.SelfBuilt True \
    --TargetResource.ClickHouseParam.DropInvalidMessage True \
    --TargetResource.ClickHouseParam.Type abc \
    --TargetResource.ClickHouseParam.BatchSize 0 \
    --TargetResource.ClickHouseParam.ConsumerFetchMinBytes 0 \
    --TargetResource.ClickHouseParam.ConsumerFetchMaxWaitMs 0 \
    --TargetResource.ClsParam.DecodeJson True \
    --TargetResource.ClsParam.Resource abc \
    --TargetResource.ClsParam.LogSet abc \
    --TargetResource.ClsParam.ContentKey abc \
    --TargetResource.ClsParam.TimeField abc \
    --TargetResource.CosParam.BucketName abc \
    --TargetResource.CosParam.Region abc \
    --TargetResource.CosParam.ObjectKey abc \
    --TargetResource.CosParam.AggregateBatchSize 1 \
    --TargetResource.CosParam.AggregateInterval 1 \
    --TargetResource.CosParam.FormatOutputType abc \
    --TargetResource.CosParam.ObjectKeyPrefix abc \
    --TargetResource.CosParam.DirectoryTimeFormat abc \
    --TargetResource.MySQLParam.Database abc \
    --TargetResource.MySQLParam.Table abc \
    --TargetResource.MySQLParam.Resource abc \
    --TargetResource.MySQLParam.SnapshotMode abc \
    --TargetResource.MySQLParam.DdlTopic abc \
    --TargetResource.MySQLParam.DataSourceMonitorMode abc \
    --TargetResource.MySQLParam.DataSourceMonitorResource abc \
    --TargetResource.MySQLParam.DataSourceIncrementMode abc \
    --TargetResource.MySQLParam.DataSourceIncrementColumn abc \
    --TargetResource.MySQLParam.DataSourceStartFrom abc \
    --TargetResource.MySQLParam.DataTargetInsertMode abc \
    --TargetResource.MySQLParam.DataTargetPrimaryKeyField abc \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.JsonKey abc \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.Type abc \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.AllowNull True \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.ColumnName abc \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.ExtraInfo abc \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.ColumnSize abc \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.DecimalDigits abc \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.AutoIncrement True \
    --TargetResource.MySQLParam.DataTargetRecordMapping.0.DefaultValue abc \
    --TargetResource.MySQLParam.TopicRegex abc \
    --TargetResource.MySQLParam.TopicReplacement abc \
    --TargetResource.MySQLParam.KeyColumns abc \
    --TargetResource.MySQLParam.DropInvalidMessage True \
    --TargetResource.MySQLParam.OutputFormat abc \
    --TargetResource.MySQLParam.IsTablePrefix True \
    --TargetResource.MySQLParam.IncludeContentChanges abc \
    --TargetResource.MySQLParam.IncludeQuery True \
    --TargetResource.MySQLParam.RecordWithSchema True \
    --TargetResource.MySQLParam.SignalDatabase abc \
    --TargetResource.MySQLParam.IsTableRegular True \
    --TargetResource.MySQLParam.SignalTable abc \
    --TargetResource.MySQLParam.DateTimeZone abc \
    --TargetResource.MySQLParam.SelfBuilt True \
    --TargetResource.PostgreSQLParam.Database abc \
    --TargetResource.PostgreSQLParam.Table abc \
    --TargetResource.PostgreSQLParam.Resource abc \
    --TargetResource.PostgreSQLParam.PluginName abc \
    --TargetResource.PostgreSQLParam.SnapshotMode abc \
    --TargetResource.PostgreSQLParam.DataFormat abc \
    --TargetResource.PostgreSQLParam.DataTargetInsertMode abc \
    --TargetResource.PostgreSQLParam.DataTargetPrimaryKeyField abc \
    --TargetResource.PostgreSQLParam.DropInvalidMessage True \
    --TargetResource.PostgreSQLParam.IsTableRegular True \
    --TargetResource.PostgreSQLParam.KeyColumns abc \
    --TargetResource.PostgreSQLParam.RecordWithSchema True \
    --TargetResource.MariaDBParam.Database abc \
    --TargetResource.MariaDBParam.Table abc \
    --TargetResource.MariaDBParam.Resource abc \
    --TargetResource.MariaDBParam.SnapshotMode abc \
    --TargetResource.MariaDBParam.KeyColumns abc \
    --TargetResource.MariaDBParam.IsTablePrefix True \
    --TargetResource.MariaDBParam.OutputFormat abc \
    --TargetResource.MariaDBParam.IncludeContentChanges abc \
    --TargetResource.MariaDBParam.IncludeQuery True \
    --TargetResource.MariaDBParam.RecordWithSchema True \
    --TargetResource.SQLServerParam.Database abc \
    --TargetResource.SQLServerParam.Table abc \
    --TargetResource.SQLServerParam.Resource abc \
    --TargetResource.SQLServerParam.SnapshotMode abc \
    --TargetResource.CtsdbParam.Resource abc \
    --TargetResource.CtsdbParam.CtsdbMetric abc \
    --TargetResource.ScfParam.FunctionName abc \
    --TargetResource.ScfParam.Namespace abc \
    --TargetResource.ScfParam.Qualifier abc \
    --TargetResource.ScfParam.BatchSize 0 \
    --TargetResource.ScfParam.MaxRetries 0 \
    --TargetResource.MqttParam.Topics abc \
    --TargetResource.MqttParam.CleanSession True \
    --TargetResource.MqttParam.Resource abc \
    --TargetResource.MqttParam.Ip abc \
    --TargetResource.MqttParam.Port 0 \
    --TargetResource.MqttParam.UserName abc \
    --TargetResource.MqttParam.Password abc \
    --TargetResource.MqttParam.Qos 0 \
    --TargetResource.MqttParam.MaxTasks 0 \
    --TargetResource.MqttParam.ServiceVip abc \
    --TargetResource.MqttParam.UniqVpcId abc \
    --TargetResource.MqttParam.SelfBuilt True \
    --TransformParam.AnalysisFormat abc \
    --TransformParam.Regex abc \
    --TransformParam.MapParam.0.Key abc \
    --TransformParam.MapParam.0.Type abc \
    --TransformParam.MapParam.0.Value abc \
    --TransformParam.FilterParam.0.Key abc \
    --TransformParam.FilterParam.0.Type abc \
    --TransformParam.FilterParam.0.MatchMode abc \
    --TransformParam.FilterParam.0.Value abc \
    --TransformParam.OutputFormat abc \
    --TransformParam.FailureParam.Type abc \
    --TransformParam.FailureParam.RetryInterval 1 \
    --TransformParam.FailureParam.MaxRetryAttempts 1 \
    --TransformParam.FailureParam.DlqType abc \
    --TransformParam.Content abc \
    --TransformParam.SourceType abc \
    --TransformParam.Result abc \
    --TransformParam.AnalyseResult.0.Key abc \
    --TransformParam.AnalyseResult.0.Type abc \
    --TransformParam.AnalyseResult.0.Value abc \
    --TransformParam.UseEventBus True \
    --PrivateLinkParam.ServiceVip abc \
    --PrivateLinkParam.UniqVpcId abc \
    --SchemaId abc \
    --TransformsParam.Content abc \
    --TransformsParam.FieldChain.0.Analyse.Format abc \
    --TransformsParam.FieldChain.0.Analyse.Regex abc \
    --TransformsParam.FieldChain.0.Analyse.InputValueType abc \
    --TransformsParam.FieldChain.0.Analyse.InputValue abc \
    --TransformsParam.FieldChain.0.SecondaryAnalyse.Regex abc \
    --TransformsParam.FieldChain.0.SMT.0.Key abc \
    --TransformsParam.FieldChain.0.SMT.0.Operate abc \
    --TransformsParam.FieldChain.0.SMT.0.SchemeType abc \
    --TransformsParam.FieldChain.0.SMT.0.Value abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Type abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Replace.OldValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Replace.NewValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Substr.Start 0 \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Substr.End 0 \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Date.Format abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Date.TargetType abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Date.TimeZone abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.RegexReplace.Regex abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.RegexReplace.NewValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Split.Regex abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.KV.Delimiter abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.KV.Regex abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.KV.KeepOriginalKey abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.Result abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.JsonPathReplace.OldValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.JsonPathReplace.NewValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperate.UrlDecode.CharsetName abc \
    --TransformsParam.FieldChain.0.SMT.0.OriginalValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Type abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Replace.OldValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Replace.NewValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Substr.Start 0 \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Substr.End 0 \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Date.Format abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Date.TargetType abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Date.TimeZone abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.RegexReplace.Regex abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.RegexReplace.NewValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Split.Regex abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.KV.Delimiter abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.KV.Regex abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.KV.KeepOriginalKey abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.Result abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.JsonPathReplace.OldValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.JsonPathReplace.NewValue abc \
    --TransformsParam.FieldChain.0.SMT.0.ValueOperates.0.UrlDecode.CharsetName abc \
    --TransformsParam.FieldChain.0.Result abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.Key abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.Operate abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.SchemeType abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.Value abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Type abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Replace.OldValue abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Replace.NewValue abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Substr.Start 0 \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Substr.End 0 \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Date.Format abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Date.TargetType abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Date.TimeZone abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.RegexReplace.Regex abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.RegexReplace.NewValue abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Split.Regex abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.KV.Delimiter abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.KV.Regex abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.KV.KeepOriginalKey abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.Result abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.JsonPathReplace.OldValue abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.JsonPathReplace.NewValue abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.ValueOperate.UrlDecode.CharsetName abc \
    --TransformsParam.FieldChain.0.AnalyseResult.0.OriginalValue abc \
    --TransformsParam.FieldChain.0.SecondaryAnalyseResult.0.Key abc \
    --TransformsParam.FieldChain.0.SecondaryAnalyseResult.0.Operate abc \
    --TransformsParam.FieldChain.0.SecondaryAnalyseResult.0.SchemeType abc \
    --TransformsParam.FieldChain.0.SecondaryAnalyseResult.0.Value abc \
    --TransformsParam.FieldChain.0.SecondaryAnalyseResult.0.OriginalValue abc \
    --TransformsParam.FieldChain.0.AnalyseJsonResult abc \
    --TransformsParam.FieldChain.0.SecondaryAnalyseJsonResult abc \
    --TransformsParam.FilterParam.0.Key abc \
    --TransformsParam.FilterParam.0.Type abc \
    --TransformsParam.FilterParam.0.MatchMode abc \
    --TransformsParam.FilterParam.0.Value abc \
    --TransformsParam.Result abc \
    --TransformsParam.SourceType abc \
    --TransformsParam.OutputFormat abc \
    --TransformsParam.RowParam.RowContent abc \
    --TransformsParam.RowParam.KeyValueDelimiter abc \
    --TransformsParam.RowParam.EntryDelimiter abc \
    --TransformsParam.KeepMetadata True \
    --TransformsParam.BatchAnalyse.Format abc \
    --TaskId abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "abc",
            "DatahubId": "abc"
        },
        "RequestId": "abc"
    }
}
```

**Example 4: 创建SINK任务(DIP Topic to ES)**



Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType SINK \
    --SourceResource.Type TOPIC \
    --SourceResource.TopicParam.Resource 12345-xxx \
    --SourceResource.TopicParam.OffsetType earliest \
    --TargetResource.Type ES \
    --TargetResource.EsParam.Resource resource-xxx \
    --TargetResource.EsParam.DropInvalidMessage True \
    --TargetResource.EsParam.Index xxx \
    --TargetResource.EsParam.DropInvalidJsonMessage False
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "abc",
            "DatahubId": "abc"
        },
        "RequestId": "abc"
    }
}
```

