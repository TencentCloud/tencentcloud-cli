**Example 1: 添加共享集群信息**

添加共享集群信息

Input: 

```
tccli trocket AddBrokerCluster --cli-unfold-argument  \
    --ClusterName rmqbroker-cd-test-providre-haohua \
    --Nameserver 21.0.207.149:9876;11.141.103.146:9876 \
    --Room rmqnamesrv-cd-test-providre-haohua \
    --AccessKey abc \
    --SecretKey abc \
    --Cpu 4 \
    --Memory 8 \
    --Disk 100 \
    --Replicas 2
```

Output: 
```
{
    "RequestId": "e246ff82-7392-45fd-a7eb-e143fd81f140",
    "Response": {
        "RequestId": "e246ff82-7392-45fd-a7eb-e143fd81f140"
    }
}
```

