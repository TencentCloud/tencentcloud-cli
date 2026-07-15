**Example 1: RequestInstancesByGet**



Input: 

```
tccli es RequestInstancesByGet --cli-unfold-argument  \
    --InstanceId es-2eosq4ee \
    --Uri _cluster/health
```

Output: 
```
{
    "Response": {
        "Detail": "{\"cluster_name\":\"es-2eosq4ee\",\"status\":\"green\",\"timed_out\":false,\"number_of_nodes\":3,\"number_of_data_nodes\":3,\"active_primary_shards\":44,\"active_shards\":88,\"relocating_shards\":0,\"initializing_shards\":0,\"unassigned_shards\":0,\"unassigned_primary_shards\":0,\"delayed_unassigned_shards\":0,\"number_of_pending_tasks\":0,\"number_of_in_flight_fetch\":0,\"task_max_waiting_in_queue_millis\":0,\"active_shards_percent_as_number\":100.0}",
        "RequestId": "38a864d1-9cee-4166-bada-a4ad6bc55411"
    }
}
```

