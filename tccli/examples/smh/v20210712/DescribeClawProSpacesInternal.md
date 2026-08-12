**Example 1: 查询实例信息**



Input: 

```
tccli smh DescribeClawProSpacesInternal --cli-unfold-argument  \
    --LibraryId smh23s*****noax2 \
    --InstanceIds ins-****7i3u \
    --Marker p0li51m9_smh314r****************bkf356w_2sQF5qKf
```

Output: 
```
{
    "Response": {
        "InstanceSpaceInfo": [
            {
                "ConsumedAt": "2026-08-09T09:29:03Z",
                "FreeEligibilityConsumed": true,
                "InstanceId": "ins-bj6e7i3u",
                "SpaceInfo": {
                    "Capacity": 53687091200,
                    "CreatedAt": "2026-08-09T09:29:03Z",
                    "FreeStorageQuota": 0,
                    "RenewFlag": "NOTIFY_EXPIRE",
                    "ResourceId": "p0mq6398_smh23sb****************gxw8r15_UirRoMbI",
                    "SpaceId": "space2******6rar9n",
                    "SpaceType": "personal",
                    "Status": "NORMAL",
                    "StorageExpiresAt": "2027-08-09T01:34:44Z",
                    "TrafficExpiresAt": "2026-09-09T09:36:49Z"
                }
            }
        ],
        "NextMarker": "p1718fjk_smh3jkm****************z3xhj91_AATplEg0",
        "RequestId": "e41b30b9-de9d-4101-b5c9-5d9b908f1545"
    }
}
```

