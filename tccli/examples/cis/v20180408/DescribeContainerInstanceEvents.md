**Example 1: 查询容器实例sshdlog的事件列表**



Input: 

```
tccli cis DescribeContainerInstanceEvents --cli-unfold-argument  \
    --InstanceName sshdlog
```

Output: 
```
{
    "Response": {
        "EventList": [
            {
                "FirstSeen": "2018-05-18T14:34:03.000+08:00",
                "LastSeen": "2018-05-18T14:34:03.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Created",
                "Message": "Created container"
            },
            {
                "FirstSeen": "2018-05-18T14:34:03.000+08:00",
                "LastSeen": "2018-05-18T14:34:03.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Pulled",
                "Message": "Successfully pulled image \"jdeathe/centos-ssh:centos-7\""
            },
            {
                "FirstSeen": "2018-05-18T14:34:03.000+08:00",
                "LastSeen": "2018-05-18T14:34:03.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Started",
                "Message": "Started container"
            },
            {
                "FirstSeen": "2018-05-18T14:33:51.000+08:00",
                "LastSeen": "2018-05-18T14:33:51.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Pulling",
                "Message": "pulling image \"jdeathe/centos-ssh:centos-7\""
            },
            {
                "FirstSeen": "2018-05-18T14:33:40.000+08:00",
                "LastSeen": "2018-05-18T14:33:40.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "SuccessfulMountVolume",
                "Message": "MountVolume.SetUp succeeded for volume \"default-token-mqfh6\" "
            },
            {
                "FirstSeen": "2018-05-18T14:33:40.000+08:00",
                "LastSeen": "2018-05-18T14:33:40.000+08:00",
                "Count": "1",
                "Level": "Warning",
                "Reason": "FailedScheduling",
                "Message": "No nodes are available that match all of the predicates: Insufficient memory (12), MatchInterPodAffinity (27)."
            },
            {
                "FirstSeen": "2018-05-18T14:33:40.000+08:00",
                "LastSeen": "2018-05-18T14:33:40.000+08:00",
                "Count": "1",
                "Level": "Normal",
                "Reason": "Scheduled",
                "Message": "Successfully assigned sshdlog-1a082ocw-cisapp to 10.0.20.45"
            }
        ],
        "RequestId": "d9b28ae4-5343-43c2-a6c1-48b716abde67"
    }
}
```

