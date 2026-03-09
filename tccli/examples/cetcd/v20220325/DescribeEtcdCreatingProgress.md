**Example 1: 查看etcd集群创建进度**



Input: 

```
tccli cetcd DescribeEtcdCreatingProgress --cli-unfold-argument  \
    --InstanceId etcd-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdefg",
        "Steps": [
            {
                "EndAt": "2020-10-02T10:54:12Z",
                "FailedMsg": "",
                "LifeState": "success",
                "StartAt": "2020-10-02T10:54:08Z",
                "Step": "prepare_env"
            },
            {
                "EndAt": "2020-10-02T10:54:15Z",
                "FailedMsg": "",
                "LifeState": "success",
                "StartAt": "2020-10-02T10:54:12Z",
                "Step": "install_suit"
            },
            {
                "EndAt": null,
                "FailedMsg": "",
                "LifeState": "running",
                "StartAt": "2020-10-02T10:54:15Z",
                "Step": "create_etcd"
            },
            {
                "EndAt": null,
                "FailedMsg": "",
                "LifeState": "pending",
                "StartAt": null,
                "Step": "install_monitor"
            },
            {
                "EndAt": null,
                "FailedMsg": "",
                "LifeState": "pending",
                "StartAt": null,
                "Step": "create_backup_policy"
            }
        ]
    }
}
```

