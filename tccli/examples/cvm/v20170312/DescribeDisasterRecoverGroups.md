**Example 1: Querying the information of a spread placement group**

This example shows you how to query the information of a spread placement group.

Input: 

```
tccli cvm DescribeDisasterRecoverGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DisasterRecoverGroupSet": [
            {
                "DisasterRecoverGroupId": "ps-21q9ibvr",
                "Name": "Database service",
                "Type": "RACK",
                "CvmQuotaTotal": 30,
                "CurrentNum": 0,
                "InstanceIds": [],
                "CreateTime": "2018-04-19T02:47:12Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c68ce193-be41-4d13-9a9b-2dc031db6477"
    }
}
```

