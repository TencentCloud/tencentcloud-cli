**Example 1: Querying placement group quota**

This example shows you how to query your placement group quota.

Input: 

```
tccli cvm DescribeDisasterRecoverGroupQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "GroupQuota": 10,
        "CvmInHostGroupQuota": 50,
        "CvmInSwGroupQuota": 20,
        "CvmInRackGroupQuota": 30,
        "CurrentNum": 25,
        "RequestId": "a13da94a-1cbc-42ca-ac6c-e14ef0c76a7c"
    }
}
```

