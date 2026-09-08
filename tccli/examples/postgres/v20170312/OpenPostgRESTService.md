**Example 1: 开启实例PostgREST服务**



Input: 

```
tccli postgres OpenPostgRESTService --cli-unfold-argument  \
    --DBInstanceId postgres-om193q01 \
    --EnableWanNet False \
    --VpcId vpc-a******r \
    --SubnetId subnet-3******i
```

Output: 
```
{
    "Response": {
        "TaskId": 100314,
        "RequestId": "0832f897-e24f-4855-8a20-2be46c2bdb5e"
    }
}
```

