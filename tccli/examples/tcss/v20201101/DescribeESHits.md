**Example 1: 获取ES查询文档列表**



Input: 

```
tccli tcss DescribeESHits --cli-unfold-argument  \
    --Query {"index":["netflow"],"body":{"query":{"bool":{"filter":{"bool":{"filter":{"range":{"timestamp":{"gte":1597075200000,"lte":1597161599999}}},"must":[],"must_not":[],"should":[]}}}},"highlight":{"fields":{"*":{}}}},"sort":[{"timestamp":"desc"}]} \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": "{\"took\":0,\"timed_out\":false,\"_shards\":{\"total\":1,\"successful\":1,\"skipped\":0,\"failed\":0},\"hits\":{\"total\":{\"value\":938,\"relation\":\"eq\"},\"max_score\":1.0,\"hits\":[{\"_index\":\"userlog-1256299843-asset_account-202026\",\"_type\":\"_doc\",\"_id\":\"PsAsunMBxgMcMHXNMzGL\",\"_score\":1.0,\"_source\":{\"id\":12900000007108,\"create_time\":\"2020-07-02T09:18:45+08:00\",\"modify_time\":\"2020-07-02T09:18:45+08:00\",\"uuid\":\"454a07be-8f21-11e9-818b-5cb9019b3cb0\",\"hostip\":\"172.21.0.14\",\"guid\":\"14f7981c-48f3-4d58-846e-fb2c86e9c7e2\",\"appid\":1256953985,\"user_name\":\"root\",\"groups\":\"root\",\"account_create_time\":\"1970-01-01T08:00:00+08:00\",\"last_login_time\":\"1970-01-01T08:00:00+08:00\",\"shell_path\":\"/bin/bash\",\"is_login_account\":1,\"is_hidden_account\":0,\"is_without_pwd\":0,\"account_privilege\":0,\"platform\":4,\"status\":0}},{\"_index\":\"userlog-1256299843-asset_account-202026\",\"_type\":\"_doc\",\"_id\":\"XMgsunMBuMj9w9DkMwS1\",\"_score\":1.0,\"_source\":{\"id\":12900000007109,\"create_time\":\"2020-07-02T09:18:45+08:00\",\"modify_time\":\"2020-07-02T09:18:45+08:00\",\"uuid\":\"454a07be-8f21-11e9-818b-5cb9019b3cb0\",\"hostip\":\"172.21.0.14\",\"guid\":\"14f7981c-48f3-4d58-846e-fb2c86e9c7e2\",\"appid\":1256953985,\"user_name\":\"bin\",\"groups\":\"bin\",\"account_create_time\":\"1970-01-01T08:00:00+08:00\",\"last_login_time\":\"1970-01-01T08:00:00+08:00\",\"shell_path\":\"/sbin/nologin\",\"is_login_account\":0,\"is_hidden_account\":0,\"is_without_pwd\":1,\"account_privilege\":1,\"platform\":4,\"status\":0}},{\"_index\":\"userlog-1256299843-asset_account-202026\",\"_type\":\"_doc\",\"_id\":\"aMgsunMBuMj9w9DkMwS-\",\"_score\":1.0,\"_source\":{\"id\":12900000007110,\"create_time\":\"2020-07-02T09:18:45+08:00\",\"modify_time\":\"2020-07-02T09:18:45+08:00\",\"uuid\":\"454a07be-8f21-11e9-818b-5cb9019b3cb0\",\"hostip\":\"172.21.0.14\",\"guid\":\"14f7981c-48f3-4d58-846e-fb2c86e9c7e2\",\"appid\":1256953985,\"user_name\":\"daemon\",\"groups\":\"daemon\",\"account_create_time\":\"1970-01-01T08:00:00+08:00\",\"last_login_time\":\"1970-01-01T08:00:00+08:00\",\"shell_path\":\"/sbin/nologin\",\"is_login_account\":0,\"is_hidden_account\":0,\"is_without_pwd\":1,\"account_privilege\":1,\"platform\":4,\"status\":0}}]}}",
        "RequestId": "e4ee7f6c-a036-43e7-b98f-96f174827fea"
    }
}
```

