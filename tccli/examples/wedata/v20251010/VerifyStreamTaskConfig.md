**Example 1: 示例1**



Input: 

```
tccli wedata VerifyStreamTaskConfig --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --TaskId ta-99703a25 \
    --TaskVersion tv-9cf782b1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": "{\"MUST_CHECK\":{\"Status\":4,\"Result\":{\"check_key_config\":\"Node mapping inconsistent: source node 1 or sink node  not found,Node mapping inconsistent: source node  or sink node 2 not found,Node  (MYSQL) missing required config: host,Node  (MYSQL) missing required config: port,Node  (MYSQL) missing required config: username,Node  (MYSQL) missing required config: password,Output node  missing DatabaseMatchRule for all database sync,Output node  missing SinkDatabaseRule for all database sync\"}}}"
        },
        "RequestId": "b13c37c6-a11c-4bdc-abe5-e0d30f42f84f"
    }
}
```

