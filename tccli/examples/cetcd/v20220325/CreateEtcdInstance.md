**Example 1: 创建etcd实例**

创建etcd实例

Input: 

```
tccli cetcd CreateEtcdInstance --cli-unfold-argument  \
    --Name etcd-cluster-1 \
    --Description examplecluster \
    --VpcId vpc-abcd1234 \
    --ServiceSubnetId subnet-abcd1234 \
    --SubnetIds subnet-abcd1234 \
    --EtcdVersion v3.4.9 \
    --Size 3 \
    --AdvancedSettings.MonitorSettings.ExistedPrometheusInstanceId prom-abcd1234 \
    --AdvancedSettings.BackupSettings.BackupInterval 300 \
    --AdvancedSettings.BackupSettings.MaxBackupCount 5 \
    --DeletionProtection True
```

Output: 
```
{
    "Response": {
        "InstanceId": "etcd-abcd1234",
        "RequestId": "51abd77d-f503-41e7-ab28-010083e02a78"
    }
}
```

