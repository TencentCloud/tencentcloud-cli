**Example 1: 查询cis-dev容器实例事件**



Input: 

```
tccli cis DescribeContainerInstanceEvent --cli-unfold-argument  \
    --InstanceName cis-dev
```

Output: 
```
{
    "Response": {
        "Event": [
            {
                "FirstSeen": "2018-05-08T15:40:41.000+08:00",
                "LastSeen": "2018-05-08T15:40:41.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Pulling",
                "Message": "pulling image \"jdeathe/centos-ssh:centos-7\""
            },
            {
                "FirstSeen": "2018-05-08T15:40:40.000+08:00",
                "LastSeen": "2018-05-08T15:40:40.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Scheduled",
                "Message": "Successfully assigned cis-84e6e50a-5b36-46cf-859d-052c73b659c7 to 172.16.3.118"
            },
            {
                "FirstSeen": "2018-05-08T15:40:44.000+08:00",
                "LastSeen": "2018-05-08T15:40:44.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Pulled",
                "Message": "Successfully pulled image \"jdeathe/centos-ssh:centos-7\""
            },
            {
                "FirstSeen": "2018-05-08T15:40:44.000+08:00",
                "LastSeen": "2018-05-08T15:40:44.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Started",
                "Message": "Started container"
            },
            {
                "FirstSeen": "2018-05-08T15:40:44.000+08:00",
                "LastSeen": "2018-05-08T15:40:44.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Created",
                "Message": "Created container"
            },
            {
                "FirstSeen": "2018-05-08T15:40:40.000+08:00",
                "LastSeen": "2018-05-08T15:40:40.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "SuccessfulMountVolume",
                "Message": "MountVolume.SetUp succeeded for volume \"default-token-ft4dl\" "
            }
        ],
        "RequestId": "12345"
    }
}
```

