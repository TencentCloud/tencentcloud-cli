**Example 1: DescribeTreeJobs**



Input: 

```
tccli oceanus DescribeTreeJobs --cli-unfold-argument  \
    --WorkSpaceId space-1257058945ap-chengdu
```

Output: 
```
{
    "Response": {
        "Children": [
            {
                "ParentId": "root",
                "Id": "folder-n130omz7",
                "Name": "test1",
                "JobSet": [
                    {
                        "JobId": "cql-ladx4cg1",
                        "Name": "test9261_1",
                        "JobType": 1,
                        "RunningCu": 0,
                        "Status": 4,
                        "ScalingType": 0,
                        "RunningCpu": 2,
                        "RunningMem": 8,
                        "DecodeSqlCode": "",
                        "PublishedJobConfigId": 139473
                    }
                ],
                "Children": null,
                "RequestId": "d9c3b849-da95-4275-83de-7f9170aa7061",
                "PageAttach": "",
                "HasMore": false
            }
        ],
        "Id": "root",
        "JobSet": [
            {
                "JobId": "cql-rvmmrqgq",
                "Name": "agent_datagen2print_test_0409",
                "JobType": 1,
                "RunningCu": 0,
                "Status": 1,
                "ScalingType": 0,
                "RunningCpu": 0,
                "RunningMem": 0,
                "DecodeSqlCode": "",
                "PublishedJobConfigId": -1
            }
        ],
        "Name": "作业列表",
        "ParentId": "",
        "RequestId": "d9c3b849-da95-4275-83de-7f9170aa7061"
    }
}
```

