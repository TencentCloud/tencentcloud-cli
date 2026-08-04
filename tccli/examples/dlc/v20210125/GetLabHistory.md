**Example 1: GetLabHistory**

获取实验室历史

Input: 

```
tccli dlc GetLabHistory --cli-unfold-argument  \
    --Id raylab-20260530151529-r6av \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ClusterId": "156",
                "ClusterName": "worker0",
                "Event": "SUCCESS",
                "FromState": "STARTING",
                "Id": 825,
                "ToState": "RUNNING",
                "TransitionTime": 1780125470846
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 4,
        "TotalPages": 1,
        "RequestId": "6909d76d-4b07-464d-b528-389b5b748b24"
    }
}
```

