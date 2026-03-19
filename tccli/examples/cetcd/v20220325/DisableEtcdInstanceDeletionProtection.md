**Example 1: 关闭etcd实例删除保护**

关闭etcd实例删除保护

Input: 

```
tccli cetcd DisableEtcdInstanceDeletionProtection --cli-unfold-argument  \
    --InstanceId etcd-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "51abd77d-f503-41e7-ab28-010083e02a78"
    }
}
```

