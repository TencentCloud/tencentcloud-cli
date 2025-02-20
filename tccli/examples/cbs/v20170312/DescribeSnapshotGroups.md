**Example 1: 查询所有快照组列表**

查询所有快照组列表

Input: 

```
tccli cbs DescribeSnapshotGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "8c068f14-5e4d-471a-ab1f-26890ada5952",
        "SnapshotGroupSet": [
            {
                "SnapshotGroupId": "csnap-csoplz7u",
                "SnapshotGroupType": "NORMAL",
                "ContainRootSnapshot": true,
                "SnapshotIdSet": [
                    "snap-31gfd8na",
                    "snap-patkqtz4",
                    "snap-1yirzaum"
                ],
                "SnapshotGroupState": "ROLLBACKING",
                "Percent": 100,
                "SnapshotGroupName": "aubreyxu2",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "Images": [],
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ImageCount": 0,
                "DeadlineTime": null,
                "IsPermanent": true
            },
            {
                "SnapshotGroupId": "csnap-orard7la",
                "SnapshotGroupType": "NORMAL",
                "ContainRootSnapshot": true,
                "SnapshotIdSet": [
                    "snap-50j8l0o8"
                ],
                "SnapshotGroupState": "NORMAL",
                "Percent": 100,
                "SnapshotGroupName": "aubreyxu1",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "Images": [
                    {
                        "ImageName": "快照组自定义镜像",
                        "ImageId": "img-nmz7p8wt"
                    }
                ],
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ImageCount": 1,
                "DeadlineTime": null,
                "IsPermanent": true
            }
        ]
    }
}
```

