**Example 1: 范例**



Input: 

```
tccli wedata ModifyTaskScript --cli-unfold-argument  \
    --ProjectId 1 \
    --IntegrationNodeDetails.0.NodeType INPUT \
    --IntegrationNodeDetails.0.Name input-MySQL-1 \
    --IntegrationNodeDetails.0.DataSourceType MYSQL \
    --IntegrationNodeDetails.0.OwnerUin  \
    --IntegrationNodeDetails.0.ExtConfig.0.Name x \
    --IntegrationNodeDetails.0.ExtConfig.0.Value 290 \
    --IntegrationNodeDetails.0.DatasourceId  \
    --IntegrationNodeDetails.0.Config.0.Name Type \
    --IntegrationNodeDetails.0.Config.0.Value MYSQL \
    --IntegrationNodeDetails.0.Description aa \
    --TaskId 20220801190325351
```

Output: 
```
{
    "Response": {
        "RequestId": "2ea96515-b3cf-4bc4-a873-302ac2cc4afd",
        "Data": {
            "Content": "/datastudio/project/1/wb555/work1/bbggg.dg"
        }
    }
}
```

