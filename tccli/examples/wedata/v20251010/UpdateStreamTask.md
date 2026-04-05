**Example 1: 示例1**



Input: 

```
tccli wedata UpdateStreamTask --cli-unfold-argument  \
    --TaskInfo.TaskName MYSQL_20260104_150303 \
    --TaskInfo.SyncType 1 \
    --TaskInfo.TaskId 585ff65b-22c1-4cc2-bc10-0e1d9c712fac \
    --TaskInfo.Nodes.0.Id 13 \
    --TaskInfo.Nodes.0.TaskId ta-ad218e6d \
    --TaskInfo.Nodes.0.Name nodeName \
    --TaskInfo.Nodes.0.NodeType INPUT \
    --TaskInfo.Nodes.0.ConnectionType KAFKA \
    --TaskInfo.Nodes.0.Description desc \
    --TaskInfo.Nodes.0.ConnectionId fac52c67-86f7-4a78-b7b5-eb9042e2d01b \
    --TaskInfo.Nodes.0.CreatorUin 12 \
    --TaskInfo.Nodes.0.OperatorUin 32 \
    --TaskInfo.Nodes.0.OwnerUin 01 \
    --TaskInfo.Nodes.0.AppId  \
    --TaskInfo.Nodes.0.WorkspaceId 13 \
    --TaskInfo.Nodes.0.Config.0.Name TopicName \
    --TaskInfo.Nodes.0.Config.0.Value topic1|test \
    --TaskInfo.Nodes.0.Config.1.Name SourceRule \
    --TaskInfo.Nodes.0.Config.1.Value regexMatch \
    --TaskInfo.Nodes.0.Config.2.Name FilterOper \
    --TaskInfo.Nodes.0.Config.2.Value insert,update,delete \
    --TaskInfo.Nodes.0.Config.3.Name StartupMode \
    --TaskInfo.Nodes.0.Config.3.Value earliest \
    --TaskInfo.Nodes.0.Config.4.Name OnceMode \
    --TaskInfo.Nodes.0.Config.4.Value At-least-once \
    --TaskInfo.Nodes.0.Config.5.Name GhostChange \
    --TaskInfo.Nodes.0.Config.5.Value false \
    --TaskInfo.Nodes.0.Config.6.Name Format \
    --TaskInfo.Nodes.0.Config.6.Value canal-json \
    --TaskInfo.Nodes.0.Config.7.Name Separation \
    --TaskInfo.Nodes.0.Config.7.Value , \
    --TaskInfo.Nodes.0.Config.8.Name TableNames \
    --TaskInfo.Nodes.0.Config.8.Value (topic1)\.null\.null\.null \
    --TaskInfo.Nodes.0.ExtConfig None \
    --TaskInfo.Nodes.0.Schema None \
    --TaskInfo.Nodes.0.NodeMapping None \
    --TaskInfo.Nodes.0.CreateTime 23 \
    --TaskInfo.Nodes.0.UpdateTime 23 \
    --TaskInfo.Config.0.Name ValidateIsCheck \
    --TaskInfo.Config.0.Value false \
    --TaskInfo.Mappings.0.SourceId 1 \
    --TaskInfo.Mappings.0.SinkId 2 \
    --TaskInfo.Incharge 700002164618 \
    --TaskInfo.InputDatasourceType MYSQL \
    --TaskInfo.OutputDatasourceType TCLake \
    --WorkspaceId space01
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "585ff65b-22c1-4cc2-bc10-0e1d9c712fac"
        },
        "RequestId": "579ff229-5fc1-4763-9c45-ac5cd02eb684"
    }
}
```

